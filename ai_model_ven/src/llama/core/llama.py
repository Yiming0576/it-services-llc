import json
from llamaapi import LlamaAPI  
import os
import sys
import attr
import logging
from llama.log.root_log import setup_logging


# Call the setup function to configure logging
setup_logging()

logger = logging.getLogger(__name__)

@attr.s
class Llama:
    """
    Represents a Llama object that interacts with the LlamaAPI.

    Args:
        user_message (str): The user message to be sent to the LlamaAPI.
        api_key (str, optional): The API key for authentication. Defaults to the value of the 'LLAMA_API_KEY' environment variable.
        role (str, optional): The role of the user. Defaults to "user".
        config_file_path (str, optional): The path to the configuration file. Defaults to 'config.json'.

    Attributes:
        user_message (str): The user message to be sent to the LlamaAPI.
        api_key (str): The API key for authentication.
        llama (LlamaAPI): The LlamaAPI instance.
        role (str): The role of the user.
        config_file_path (str): The path to the configuration file.
        api_request_json (dict): The API request JSON structure with the configured parameters.
    """

    user_message = attr.ib()
    api_key = attr.ib(default=os.getenv('LLAMA_API_KEY'))  # Encapsulated variable for API key
    llama = attr.ib(init=False)
    role = attr.ib(default="user")
    config_file_path = attr.ib(default='config.json')
    api_request_json = attr.ib(init=False)

    def __attrs_post_init__(self):
        """
        Initializes the Llama object by creating a LlamaAPI instance and setting the API request JSON structure.
        """
        self.llama = LlamaAPI(self.api_key) if self.api_key else None
        self.api_request_json = self._initialize_api_config()

    def _initialize_api_config(self):
        """
        Initializes the API configuration by loading the configuration file and setting the necessary parameters.

        Returns:
            dict: The API request JSON structure with the configured parameters.
        """
        # Define default API request JSON structure
        api_request_json = {
            "messages": [
                {
                    "role": self.role,
                    "content": self.user_message
                }
            ],
            "functions": [], 
            "model": "",  
            "stream": "", 
            "max_token": "", 
            "temperature": "",
            "top_p": "",
            "frequency_penalty": ""
        }

        self.config_file_path = os.getcwd() + f"/llama/config/{self.config_file_path}"
        
        # Load the configuration file
        if os.path.exists(self.config_file_path):
            # File exists, so open it and load the configuration
            with open(self.config_file_path, 'r') as config_file:
                config = json.load(config_file)
                logger.debug(f"Config File Contains: {config}")
        else:
            logger.error(f"The configuration file '{self.config_file_path}' does not exist.")
            # Handle this error scenario as needed
            return None

        # Set functions by extracting from config
        functions = config.get('functions', [])
        for function in functions:
            function_call = {
                "name": function.get('name', ''),
                "parameters": {
                    "type": "object",
                    "properties": function.get('parameters', {})
                },
                "required": function.get('required', [])
            }
            
            api_request_json['functions'].append(function_call)

        # Set the model from config
        api_request_json["model"] = config.get("model", "")
        api_request_json["stream"] = config.get("stream", False)
        api_request_json["max_token"] = config.get("max_token", 500)
        api_request_json["temperature"] = config.get("temperature", 0.2)
        api_request_json["top_p"] = config.get("top_p", 1.0)
        api_request_json["frequency_penalty"] = config.get("frequency_penalty", 1.0)

        return api_request_json

    def execute_request(self):
        """
        Executes the API request using the LlamaAPI instance and returns the response.

        Returns:
            dict: The response received from the API.
        """
        try:
            logger.debug("Sending API request:")
            # logger.debug(json.dumps(self.api_request_json, indent=2))

            if self.llama:
                # Execute the request using your SDK or library (assuming llama.run() exists)
                response = self.llama.run(self.api_request_json)
                print(f"Response: {response}")

                # Log the response received
                logger.debug("API request successful")
                logger.debug(f"Response received: {response}")
                # logger.debug(json.dumps(response, indent=2))

                return response
            else:
                logger.error("LlamaAPI instance not initialized.")
                return None

        except Exception as e:
            logger.error(f"Error executing API request: {str(e)}")
            # Handle the error appropriately, e.g., retry, notify user, etc.
            return None

# Example usage:
# if __name__ == "__main__":
#     # Accessing the API key
#     api_key = os.getenv('LLAMA_API_KEY')

#     if api_key is None:
#         logger.error("API_KEY environment variable not set")
#         sys.exit(1)  # Exit the program if API_KEY is not set

#     # Create an instance of LlamaAPI
#     api_client = Llama("What is the weather today?")

#     # Execute the API request
#     response = api_client.execute_request()
#     print(f"Response: {response}")

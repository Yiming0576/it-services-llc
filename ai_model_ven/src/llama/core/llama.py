import json
import os
import logging
import asyncio
import attr
from llamaapi import LlamaAPI
import sys

# Configure logging
logging.basicConfig(
    filename='llama/log/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)
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
    api_key = attr.ib(default=os.getenv('LLAMA_API_KEY'))
    llama = attr.ib(init=False)
    role = attr.ib(default="user")
    config_file_path = attr.ib(default='config.json')
    api_request_json = attr.ib(init=False)

    def __attrs_post_init__(self):
        """
        Initializes the Llama object by creating a LlamaAPI instance and setting the API request JSON structure.
        """
        self.llama = LlamaAPI(self.api_key) if self.api_key else None
        self.api_request_json = self.load_request_config_json()
        logger.debug("Initializing Llama object")
        logger.debug(f"api_request_json:  {self.api_request_json}")
        self.update_request_config()


    def load_request_config_json(self):
        """
        Loads the request configuration from the JSON file specified by the config_file_path.
        
        Returns:
            dict: The API request JSON structure.
        """
        self.config_file_path = os.path.join(os.getcwd(), "llama", "config", self.config_file_path)
        try:
            with open(self.config_file_path, 'r') as config_file:
                self.api_request_json = json.load(config_file)
            logger.info(f"Loaded configuration from: {self.config_file_path}")
            logger.debug(f"Configuration data: {self.api_request_json}")
            return self.api_request_json
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_file_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from configuration file: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error loading configuration file: {e}")
            raise

    def update_request_config(self):
        """
        Updates the request configuration with new values for specific keys.

        Args:
            key (str): The key to be updated.
            value (str): The new value for the key.
        """
        logger.debug("Updating request configuration")
        self.api_request_json["messages"][0]["role"] = self.role
        self.api_request_json["messages"][0]["content"] = self.user_message
        logger.info(f"Updated configuration: {self.api_request_json}")

    def execute_request(self):
        """
        Executes the API request using the LlamaAPI instance and returns the response.

        Returns:
            dict: The response received from the API.
        """
        logger.debug("Preparing to execute API request")
        try:
            if self.llama:
                logger.debug(f"User message: {self.user_message}")

                logger.debug(f"Sending API request: {self.api_request_json}")
                response =  self.llama.run(self.api_request_json)
                logger.info(f"Received response: { response.json()}")
                
                return response.json()
            else:
                logger.error("LlamaAPI instance not initialized.")
                return None
        except Exception as e:
            logger.error(f"Error executing API request: {e}")
            return None

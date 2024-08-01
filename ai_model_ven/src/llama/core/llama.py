import json
import logging
from llamaapi import LlamaAPI  
import os
import attr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#logger.info("Logger initialized.")  # Example log message

@attr.s
class Llama:
    user_message = attr.ib()
    api_key = attr.ib(default=os.getenv('LLAMA_API_KEY'))
    llama = attr.ib(init=False)
    context = attr.ib(default=None)
    role = attr.ib(default="user")
    config_file_path = attr.ib(default='config.json')
    api_request_json = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.llama = LlamaAPI(self.api_key) if self.api_key else None
        logger.debug(f"LlamaAPI instance: {self.llama}")
        self.api_request_json = self._initialize_api_config()
        if self.context:
            self.api_request_json['messages'].extend(self.context)

    def _initialize_api_config(self):
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
            "max_token": 8000, 
            "temperature": .1,
            "top_p": 1.0,
            "frequency_penalty": 1.0
        }

        config_file_path = os.path.join(os.getcwd(), "ai_model_ven", "src", "llama", "config", self.config_file_path)
        #logger.info(f"Constructed config file path: {self.config_file_path}")

        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as config_file:
                config = json.load(config_file)
                #logger.info(f"Config File Contains: {config}")
                
                api_request_json.update({
                    "model": config.get("model", ""),
                    "stream": config.get("stream", ""),
                    "max_token": config.get("max_token", 8000),
                    "temperature": config.get("temperature", 0.1),
                    "top_p": config.get("top_p", 1.0),
                    "frequency_penalty": config.get("frequency_penalty", 1.0),
                })
                
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
        else:
            logger.error(f"The configuration file '{config_file_path}' does not exist.")
            return None

        return api_request_json


    def add_message(self, role="user"):
        self.api_request_json['messages'].append({
            "role": role,
            "content": self.user_message
        })


    def execute_request(self):
        if not self.llama:
            logger.error("LlamaAPI instance not initialized.")
            return None

        try:
            #logger.info("Sending API request:")
            message = self.api_request_json.get('messages', [])
            # for m in message:
            #     print(f"Role: {m.get('role')}")
            #     print(f"Content: {m.get('content')}")
            #     print()
            response = self.llama.run(self.api_request_json).json()
            # Check if the response is a stream or needs different handling
            if isinstance(response, (str, dict)):  # Handle if response is JSON or string
                #logger.info("Response received:\n%s", json.dumps(response, indent=4))
                choices = response.get('choices')
                print(choices[0]['message']['content'])
                return response
            else:
                logger.warning("Received unexpected response type.")
                return None
        except Exception as e:
            logger.error(f"Error executing API request: {str(e)}")
            return None
        
    def update_user_message(self, msg):
        self.user_message = msg
        if self.api_request_json and "messages" in self.api_request_json:
            self.api_request_json["messages"].append({
                "role": self.role,
                "content": self.user_message
            })
        else:
            logger.error("API request JSON is not properly initialized or messages are missing")

if __name__ == "__main__":
    api_key = "LL-yAOWPfOpKp5DaXnHpJD8L46AXw4uKRC0kcnHQH9toSzf4tuDzM9MJvxaYz2MOjJZ"
    api_client = Llama("What is the weather today?", api_key=api_key)
    response = api_client.execute_request()
    # for choice in response.get('choices'):
    #     print(choice['message']['content'])

    # choices = response.get('choices')
    # print(choices[0]['message']['content'])
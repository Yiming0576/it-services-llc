import os
import sys
import logging
import json
from llama.core.llama import Llama

# Basic configuration for logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Logger initialized.")  # Example log message

def main():
    if api_key is None:
        logger.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set

    client = Llama(api_key=api_key, user_message="")

    while True:
        user_input = input("Type your message or enter Q to quit: ")
        if user_input.upper() == "Q":
            break

        client.update_user_message(user_input)
        response = client.execute_request()

        if response:
            response_json = json.dumps(response, indent=2)
            print(response_json)
        else:
            logger.error("No response from Llama API")

if __name__ == "__main__":
    # Accessing the API key
    api_key = "LL-yAOWPfOpKp5DaXnHpJD8L46AXw4uKRC0kcnHQH9toSzf4tuDzM9MJvxaYz2MOjJZ"
    main()
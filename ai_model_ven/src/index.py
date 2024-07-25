import os
import sys
# import plugnplai as pl
from llama.core.llama import Llama
from llama.log.root_log import setup_logging


# Call the setup function to configure logging
setup_logging()

import logging
logger = logging.getLogger(__name__)

def main()-> None:

    model = input("What AI model would you like to know more about?\n"
                " << Claude (1) >>\n"
                " << Google Gemini (formerly Bard) (2) >>\n"
                " << Microsoft Copilot (3) >>\n"
                " << Perplexity (4) >>\n"
                " << ChatSonic (5) >>\n"
                " << OpenAI ChatGPT (6) >>\n"
                " << Character.AI (7) >>\n"
                " << xAI Grok (8) >>\n"
                " << Meta AI (LLAMA) (9) >>\n"
                "Enter the corresponding number: ")

    match model:
        case 1:
            print("Integrates well with social platforms for enhanced interactions.")

        case 2:
            print("Allows for customization and experimentation with AI models.")

        case 3:
            print("Developed by Anthropic, Claude is known for its human-like interactions and strong reasoning capabilities.")

        case 4:
            print("Great for problem-solving and multimodal capabilities.")

        case 5:
            print("You can become a mobile app developer")
        case 6:
            print("You can become a mobile app developer")

        case 7:
            print("You can become a mobile app developer")

        case 8:
            print("You can become a mobile app developer")
        case 9:
            print("You can become a mobile app developer")
        case _:
            print("The language doesn't matter, what matters is solving problems.")

# Example usage:
if __name__ == "__main__":
    # Accessing the API key
    api_key = os.getenv('LLAMA_API_KEY')

    if api_key is None:
        logger.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set


    # user input testing porpuse
    # user_input = input("Enter your question: ")

    # Create an instance of LlamaAPI
    api_client = Llama(" 1 + 1 ?")

    # Execute the API request
    response = api_client.execute_request()
    logger.debug(f"Response: {response}")


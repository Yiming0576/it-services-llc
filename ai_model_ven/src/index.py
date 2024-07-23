import os
import sys
import logging
import plugnplai as pl
from llama import Llama



def main()-> None:

    model = input("What AI model would you like it: \n << LLAMA (1) >>\n << ChatGPT (1) >>? ")

    match model:
        case 1:
            print("You can become a web developer.")

        case 2:
            print("You can become a Data Scientist")

        case 3:
            print("You can become a backend developer")
        
        case 4:
            print("You can become a Blockchain developer")

        case 5:
            print("You can become a mobile app developer")
        case _:
            print("The language doesn't matter, what matters is solving problems.")

# Example usage:
if __name__ == "__main__":
    # Accessing the API key
    api_key = os.getenv('LLAMA_API_KEY')

    if api_key is None:
        logging.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set

    # Create an instance of LlamaAPI
    api_client = Llama("What is the weather today?")

    # Execute the API request
    response = api_client.execute_request()
    print(f"Response: {response}")


import os
import sys
# import plugnplai as pl
from llama.core.llama import Llama
# from llama.log.root_log import setup_logging
import logging
import json




def llama_driver():
    api_key = os.getenv('LLAMA_API_KEY')

    if api_key is None:
        logging.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set


    flag = True
    api_client = Llama() 

    while flag:
        # Get user input
        user_input = input("(exit: q)Enter your message or content: ")
        api_client.user_input(user_input)

        # Execute the API request
        response_json =  api_client.execute_request()
        # response_content = response_json['choices'][0]['message']['content']
        print(f"Question: {api_client.user_message}")
        # print("Type of response content: ", type(response_content))
        # print(f"Response Content: {response_content}")
        format_json = json.dumps(response_json, indent=4)
        print(f"Response json: {format_json}")

        if user_input.lower() == 'q':
            flag = False
            print("Exiting the program...")
            break


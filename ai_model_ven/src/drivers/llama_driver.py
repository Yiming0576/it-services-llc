import json
import os
import logging
import sys
from datetime import datetime
from llama.core.llama import Llama
from model.record import Record
from model.chatsession import ChatSession

record = Record() 

def insert_Record():
    """Insert a new record to the database."""
    pass

def llama_driver():
    api_key = os.getenv('LLAMA_API_KEY')

    if api_key is None:
        logging.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set
    
    # Initialize the Llama API client
    flag = True
    api_client = Llama.get_instance()

    while flag:
        # Get user input
        user_input = input("(exit: q) Enter your message or content: ")
        if user_input.lower() == 'q':
            print("Exiting the program...")
            break

        api_client.user_message = user_input
        api_client.update_request_config()
        logging.debug(f"User message: \n ========================\n{api_client.user_message}")

        # Execute the API request
        response_json = api_client.execute_request()

        if response_json:
            # Print the response JSON in a formatted way
            format_json = json.dumps(response_json, indent=4)
            print(f"Response JSON: {format_json}")

            # Access the response content
            try:
                response_content = response_json['choices'][0]['message']['content']
                print(f"Response from the API: {response_content}")
            except KeyError as e:
                logging.error(f"KeyError: {e}")
                response_content = "Error extracting response content."

            # Create and add a chat session record
            chat_session = ChatSession(
                user_input=user_input,
                chatbot_response=format_json,
                end_time=datetime.now()
            )

            record.add_session(chat_session)

            # If needed, update the end time and duration of the chat session
            chat_session.end_session()

            # logging(f"Chat Session ID: {chat_session.session_id}")

        else:
            logging.error("Failed to get a response from the API")
import os
import sys
import logging
import json
from llama.core.llama import Llama

# Basic configuration for logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#logger.info("Logger initialized.")  # Example log message


def save_context_to_file(context, filename="conversation_context.json"):
    with open(filename, "w") as f:
        json.dump(context, f)

def load_context_from_file(filename="conversation_context.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {"questions": [], "responses": []}

def clear_context_file(filename="conversation_context.json"):
    with open(filename, "w") as f:
        json.dump({"questions": [], "responses": []}, f)

def main():
    if api_key is None:
        logger.error("API_KEY environment variable not set")
        sys.exit(1)  # Exit the program if API_KEY is not set


    cont = load_context_from_file()

    prev_context = [{"role": "user", "content": q} for q in cont.get("questions", [])]
    prev_context += [{"role": "assistant", "content": r} for r in cont.get("responses", [])]
    client = Llama(user_message="", api_key=api_key, context=prev_context)

    while True:
        user_input = input("Type your message or enter Q to quit: ")
        if user_input.upper() == "Q":
            user_input = input("Would you like to continue this conversation later? (Y/N): ")
            if user_input.upper() == "Y":
                save_context_to_file(cont)
            else:
                clear_context_file()
            break


        client.update_user_message(user_input)
        client.add_message()
        response = client.execute_request()

        if response:
            cont["questions"].append(user_input)
            cont["responses"].append(response['choices'][0]['message']['content'])
            print()
        else:
            logger.error("No response from Llama API")

if __name__ == "__main__":
    # Accessing the API key
    api_key = "LL-yAOWPfOpKp5DaXnHpJD8L46AXw4uKRC0kcnHQH9toSzf4tuDzM9MJvxaYz2MOjJZ"
    main()
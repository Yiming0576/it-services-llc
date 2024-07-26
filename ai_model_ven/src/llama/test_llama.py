from llamaapi import LlamaAPI
import json
import os
import sys

# Accessing the API key
api_key = os.getenv('LLAMA_API_KEY')

if api_key is None:
    print("API_KEY environment variable not set")
    sys.exit(1)  # Exit the program if API_KEY is not set
llama = LlamaAPI(api_key)

content = input("Enter the content of the message: ")
api_request_json = {
    "model": "llama3.1-405b",
  "messages": [
    {"role": "user", "content": content},
  ],
  "stream": False,
}

# Make your request and handle the response
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
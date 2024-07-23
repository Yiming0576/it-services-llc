# Llama Model Documentation

## Overview

This document provides comprehensive guidance on configuring the Llama3-70b model and setting up the API, including managing the LLAMA API key securely.

## Setting LLAMA API Key in Environment Variables

### Introduction

To ensure secure handling of sensitive information like API keys and credentials, this guide walks you through exporting your LLAMA API key into environment variables across different operating systems.

### Prerequisites

Before proceeding, make sure you have the following:

- **LLAMA API Key:** Obtain your API key from the LLAMA developer portal or your account settings.
- **Terminal or Command Prompt:** Access to a terminal or command prompt on your operating system.

## Instructions

### Mac/Linux

1. **Open Terminal:**
   - Use Terminal on Mac (found in Applications/Utilities) or your preferred terminal emulator on Linux (e.g., GNOME Terminal, Konsole).

2. **Edit ~/.bashrc or ~/.bash_profile:**
   - Open your terminal and edit the Bash configuration file:
     ```
     nano ~/.bashrc
     ```
     or
     ```
     nano ~/.bash_profile
     ```
   - Add the following line at the end of the file:
     ```
     export LLAMA_API_KEY="your_llama_api_key_here"
     ```
   - Replace `"your_llama_api_key_here"` with your actual LLAMA API key.

3. **Save and Apply Changes:**
   - Exit nano by pressing `Ctrl + X`, confirm changes with `Y`, and save by pressing `Enter`.
   - Apply the changes immediately by running:
     ```
     source ~/.bashrc
     ```
     or
     ```
     source ~/.bash_profile
     ```

4. **Verify:**
   - To verify if the key was correctly set, echo the variable:
     ```
     echo $LLAMA_API_KEY
     ```
   - It should display your API key.

### Windows

1. **Open Command Prompt:**
   - Search for "Command Prompt" in the Start Menu and open it.

2. **Set Environment Variable:**
   - Set the environment variable using the following command:
     ```
     setx LLAMA_API_KEY "your_llama_api_key_here"
     ```
   - Replace `"your_llama_api_key_here"` with your actual LLAMA API key.

3. **Verify:**
   - To verify if the key was correctly set, echo the variable:
     ```
     echo %LLAMA_API_KEY%
     ```
   - It should display your API key.

## Conclusion

By following these steps, you have successfully configured your LLAMA API key in environment variables, ensuring secure storage and accessibility for your applications. Remember to treat your API key as confidential and avoid exposing it in public repositories or untrusted environments.

## Configuration

### Model Details

- **Model Name:** llama3-70b
- **Stream Mode:** False
- **Max Tokens:** 500
- **Temperature:** 0.1
- **Top P:** 1.0
- **Frequency Penalty:** 1.0

### Functions

The model supports various functions that enhance its capabilities. Refer to the model documentation for detailed function descriptions and usage.

## Usage

Initialize the model with the provided configuration to utilize its features effectively.

```json
{
    "model": "llama3-70b",
    "stream": false,
    "max_token": 500,
    "temperature": 0.1,
    "top_p": 1.0,
    "frequency_penalty": 1.0,
    "functions": [
        // List of functions supported by the model
    ]
}

```
### Example: Generating Text
```python
# Example Python code to generate text using the model
from llama import Llama
import os
import logging
import sys

# Accessing the API key
api_key = os.getenv('LLAMA_API_KEY')

if api_key is None:
    logging.error("API_KEY environment variable not set")
    sys.exit(1)  # Exit the program if API_KEY is not set

# Create an instance of LlamaAPI with the question
api_client = Llama("What is the weather today?")

# Execute the API request
api_client.execute_request()

```


# AI Chatbot using Google Gemini API

## Overview

A Python-based AI chatbot that leverages Google's Gemini API to provide intelligent and context-aware conversational responses. The chatbot supports conversation history, command handling, colored terminal output, and environment-based configuration for secure API key management.

## Features

* Google Gemini AI integration
* Interactive command-line interface (CLI)
* Session-based conversation memory
* Chat history management
* Colored terminal output
* Environment variable configuration
* Logging and error handling
* Easy setup and deployment

## Project Structure

```text
chatbot/
├── main.py
├── chatbot.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md
└── utils/
    ├── helpers.py
    └── logger.py
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory and add your Gemini API key:

```env
API_PROVIDER=gemini
GEMINI_API_KEY=your_api_key_here
LOG_LEVEL=INFO
ENABLE_LOGGING=True
MAX_HISTORY_LENGTH=10
```

### Get a Gemini API Key

1. Visit Google AI Studio.
2. Create a new API key.
3. Copy the key into your `.env` file.

## Running the Application

```bash
python main.py
```

## Available Commands

| Command    | Description                |
| ---------- | -------------------------- |
| `/help`    | Show available commands    |
| `/clear`   | Clear conversation history |
| `/history` | Display chat history       |
| `/quit`    | Exit the chatbot           |
| `exit`     | Exit the chatbot           |
| `bye`      | Exit the chatbot           |

## Example

```text
You: Hello
Bot: Hi! How can I assist you today?

You: Explain Python
Bot: Python is a high-level programming language known for its simplicity and readability.
```

## Technologies Used

* Python 3.x
* Google Gemini API
* python-dotenv
* Colorama
* Logging Module

## Security

* API keys are stored securely using environment variables.
* `.env` is excluded from version control using `.gitignore`.
* `.env.example` is provided as a configuration template.

## Future Enhancements

* GUI Version using Tkinter or CustomTkinter
* Voice Input and Output
* Chat History Export
* Multiple AI Model Support
* Web-Based Interface

## Author

Nihith

## License

This project is licensed under the MIT License.

## ⭐ Support the Project

If you find this project useful, please consider giving it a star on GitHub. It helps increase visibility and motivates further development.

⭐ Star the repository here:

[https://github.com/YOUR_USERNAME/YOUR_REPO_NAME](https://github.com/nihith2912/chatbot.git)
Thank you for your support!


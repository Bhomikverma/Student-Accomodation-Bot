
# Student Accommodation Chatbot

This is a chatbot designed to assist students with accommodation-related queries. It is deployed using [Hugging Face Spaces] and built with the following technologies:

## Features

- **LLM-Powered Conversations**: Uses the Mistral API via [OpenRouter](https://openrouter.ai) for natural language understanding.
- **Chat Memory**: Remembers context throughout the conversation for a more human-like interaction.
- **Gradio Interface**: Simple, elegant UI built using Gradio.
- **Save Chat Functionality**: Users can download the full conversation. Each file includes a unique timestamp to avoid overwriting.
  
## Tech Stack

- **Language Model**: Mistral via OpenRouter
- **Frontend/UI**: [Gradio](https://www.gradio.app/)
- **Backend**: Python
- **Hosting**: Hugging Face Spaces

## Live Demo

👉 Try it here: [Student Accommodation Chatbot on Hugging Face](https://huggingface.co/spaces/bhomikk/student-accommodation-bot)

## How to Run Locally

```bash
git clone https://github.com/YOUR-USERNAME/student-accommodation-chatbot.git
cd student-accommodation-chatbot
pip install -r requirements.txt
python app.py

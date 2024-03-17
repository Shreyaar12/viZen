# viZen: Welcome to your personalized mental health journey

This project is a web-based chatbot application powered by OpenAI's GPT-3.5 API and leverages the `SpeechRecognition` API in Webkit-based browsers such as Chrome for voice input. The chatbot is designed to offer conversational interactions and can provide advice, general information, and a friendly response, emulating a "big sister" persona in a zero-shot prompting manner.

## Features

- Text chat interface with OpenAI's GPT-3.5 model
- Speech-to-text functionality for inputting messages via voice
- Text-to-speech to read the chatbot responses out loud
- Zero-shot prompting, meaning the chatbot doesn't require any pre-training or specific prompts to engage in a conversation

## Project Structure

```
CHATGPT API
│
├── static
│   ├── assets
│   │   ├── css
│   │   ├── fonts
│   │   ├── images
│   │   └── js
│   ├── images
│   │   ├── facebook.png
│   │   ├── OIG3.jpg
│   │   └── v960-ning-05.jpg
│   ├── style
│   │   └── vendor
│   └── style.css
│
├── templates
│   ├── chatbot.html
│   └── index.html
│
├── .env
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or above.
- You have a Windows/Linux/Mac machine.
- You have installed all Python libraries listed in `requirements.txt`.
- You have a web browser, preferably Chrome, for the best speech recognition support.
- You have an API key from OpenAI for accessing the GPT-3.5 model.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the cloned directory.
3. Install the required Python libraries:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content, replacing `your_openai_api_key` with your actual OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Replace the placeholder for the OpenAI API key in `app.py` with your key or configure it to read from the `.env` file.

## Running the Application

To run the application, execute the following command in the terminal:

```sh
python app.py
```

The application will be available at [http://localhost:8000](http://localhost:8000) in your web browser.

## Using the Chatbot

1. Open your web browser and go to [http://localhost:8000](http://localhost:8000).
2. Use the text input to type your message or click on "Speak Up!" to use voice input.
3. Press "Send" to submit your message to the chatbot.
4. Wait for the chatbot's reply, which will be spoken out loud and displayed in the chat interface.

For the best experience, use Google Chrome as your web browser.

## Documentation

For more information on the technologies used and how to work with them, refer to the following documentation:

- [OpenAI API](https://beta.openai.com/docs/)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)


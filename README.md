# AI-Powered Voice Assistant

A voice-activated personal assistant using NLP and speech recognition.

## Features
- Speech-to-text using SpeechRecognition
- Text generation using GPT-2
- Weather updates
- Web searches
- Real-time interaction

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Get an OpenWeatherMap API key from https://openweathermap.org/api
2. Create a `.env` file in the project root and add your API key:
```
WEATHER_API_KEY=your_api_key_here
```

## Usage

Run the assistant:
```bash
python assistant.py
```

### Commands
- Ask about weather: "What's the weather in [location]?"
- Web search: "Search for [query]"
- General conversation: "Tell me about..."

## Requirements
- Python 3.7+
- Microphone
- Internet connection

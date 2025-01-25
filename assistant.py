import os
import speech_recognition as sr
from transformers import pipeline
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.generator = pipeline('text-generation', model='gpt2')
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        
    def listen(self):
        """Capture audio and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that")
                return None
            except sr.RequestError:
                print("Speech service unavailable")
                return None

    def generate_response(self, prompt):
        """Generate text response using GPT-2"""
        response = self.generator(prompt, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']

    def get_weather(self, location):
        """Get current weather for a location"""
        if not self.weather_api_key:
            return "Weather API key not configured"
            
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{data['weather'][0]['description']}, {data['main']['temp']}°C"
        return "Could not fetch weather data"

    def web_search(self, query):
        """Perform a web search"""
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json()
            if results['RelatedTopics']:
                return results['RelatedTopics'][0]['Text']
        return "No results found"

    def run(self):
        """Main interaction loop"""
        print("Voice Assistant ready!")
        while True:
            command = self.listen()
            if command:
                if "weather" in command.lower():
                    location = command.split("in")[-1].strip()
                    response = self.get_weather(location)
                elif "search" in command.lower():
                    query = command.split("for")[-1].strip()
                    response = self.web_search(query)
                else:
                    response = self.generate_response(command)
                print(f"Assistant: {response}")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()

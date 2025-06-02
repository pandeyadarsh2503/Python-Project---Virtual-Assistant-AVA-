# Python-Project---Virtual-Assistant-AVA-
# AVA - Voice Assistant

A simple Python-based voice assistant named **AVA** that can perform various tasks such as searching Wikipedia, opening websites, telling time, fetching weather information, performing Google searches, and shutting down the computer—all through voice commands.

## Features

- Greets the user based on the time of day.
- Listens to voice commands and recognizes speech using Google Speech Recognition.
- Searches Wikipedia and reads out summaries.
- Opens YouTube and Google in the browser.
- Announces the current time.
- Fetches weather information for a specified city using the Weatherstack API.
- Performs Google searches and displays results.
- Shuts down the computer on command.
- Supports quit/exit commands to stop the assistant.

## Technologies Used

- Python 3.x
- `pyttsx3` for text-to-speech
- `speech_recognition` for speech-to-text
- `wikipedia` API for searching Wikipedia
- `webbrowser` module to open websites
- `requests` and `BeautifulSoup` for web scraping Google search results and weather data
- `datetime` for time-based greetings and time reporting
- `os` module for system commands (shutdown)

## Setup & Installation

1. Clone the repository:

   ```bash
   https://github.com/pandeyadarsh2503/Python-Project---Virtual-Assistant-AVA-.git
   cd ava-voice-assistant

## Install required dependencies:
    pip install pyttsx3 speechrecognition wikipedia requests beautifulsoup4

## How to Run:
    python your_script_name.py

## Usage
Example voice commands:
- "Wikipedia Albert Einstein"
- "Open YouTube"
- "Open Google"
- "What is the time?"
- "What's the weather?"
- "Search on Google for latest AI news"
- "Shut down"
- "Quit" or "Exit"




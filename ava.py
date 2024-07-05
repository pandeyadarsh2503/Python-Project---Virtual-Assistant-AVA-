import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio,rate = 175):
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Request Error:", err)

def parse_search_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    results = soup.find_all('div', class_='tF2Cxc')

    for index, result in enumerate(results, start=1):
        title = result.find('h3').get_text()
        link = result.find('a')['href']
        print(f"{index}. {title} - {link}\n")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    print("Hi! I am AVA !!! How can I help you today?")
    speak("Hi! I am AVA !!! How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said:{query}\n')

    except Exception as e:
        
        print("Say that again please...")
        speak("Say that again please")
        return 'None'
    return query

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,
        'query': city
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temperature']
        weather_description = weather_data['current']['weather_descriptions'][0]
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't fetch the weather information. Please try again later."
    
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube Sir,")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google Sir,")
            webbrowser.open("google.com")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {time}")
            speak(f'Sir, the time is {time}')
        
        elif 'weather' in query:
            api_key = '6f9c6496403400f57c4fded4f46cad0c'
            city = speak("Enter the city name: ")
            city = takeCommand().lower()
            result = get_weather(api_key, city)
            print(result)
            speak(result)

        elif "on google" in query:
            a = query
            search_results = google_search(a)
            parse_search_results(search_results)
        
        elif "shut down" in query:
            speak("Shutting Computer down Sir")
            os.system("shutdown /s /t 1")

        elif "quit" or "exit" in query:
            exit()


        


        
            

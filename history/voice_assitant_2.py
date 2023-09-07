import speech_recognition as sr
import os
import webbrowser
import pyttsx3

# Initialize the speech recognition engine
engine = sr.Recognizer()

# Initialize the text-to-speech engine
#voice = pyttsx3.init()

# Define a function to open an app in Windows
def open_app(app_name):
    os.system("start " + app_name)

# Define a function to open YouTube in a browser
def open_youtube():
    print("opening youtube")
    webbrowser.open("https://www.youtube.com/")

# Define a function to play music in Windows
def play_music(music_file):
    os.system("start " + music_file)

# Start the voice assistant
print("Hello, I am Jarvis. How can I help you?")

# Continuously listen for user input
while True:
    # Record audio from the microphone
    #audio = engine.listen(source="microphone")
    text = ""
    with sr.Microphone() as source:
        print('Say Something')
        audio = engine.listen(source)
        print(audio) #This is just a speech_recognition.AudioData object
        text = engine.recognize_google(audio) #Speech to text google recognizer
        text = text.lower()
        print(text, type(text)) #This is what you actually said

    # Try to recognize the speech in the audio
    text = engine.recognize_google(audio)

    # If the speech was recognized, process the command
    if text:
        # Check if the user wants to open an app
        if "open" in text:
            app_name = text.split("open")[1]
            open_youtube()
            open_app(app_name)

        # Check if the user wants to open YouTube
        elif "youtube" in text:
            open_youtube()

        # Check if the user wants to play music
        elif "play" in text:
            music_file = text.split("play")[1]
            play_music(music_file)
        elif "exit" in text:
            break

    # Otherwise, ask the user to repeat themselves
    else:
        print("I didn't understand that. Can you please repeat yourself?")

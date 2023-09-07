import speech_recognition as sr
import webbrowser
import os

def open_app(app_name):
    # Get the app name from the user.
    app_name = app_name.lower()

    # Try to open the app.
    try:
        os.system("start " + app_name)
    except:
        print("Could not open app.")

def open_youtube():
    # Open YouTube in a browser.
    webbrowser.open("https://www.youtube.com/")

def play_music():
    # Play music in Windows.
    os.system("start /min wmplayer")

# Create a voice recognition object.
r = sr.Recognizer()

# Get the audio from the microphone.
with sr.Microphone() as source:
    audio = r.listen(source)

# Try to recognize the speech.
try:
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Could not understand speech.")

# Get the user's command.
command = text.lower()

# Handle the user's command.
if "open" in command:
    open_app(command.replace("open", ""))
elif "youtube" in command:
    open_youtube()
elif "music" in command:
    play_music()

# Print a message to the user.
print("Jarvis is ready to help.")

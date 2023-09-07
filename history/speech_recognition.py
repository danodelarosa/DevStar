import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something')
    audio = r.listen(source)
    print(audio) #This is just a speech_recognition.AudioData object
    text = r.recognize_google(audio) #Speech to text google recognizer
    print(text) #This is what you actually said
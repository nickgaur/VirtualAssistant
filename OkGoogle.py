import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice", voices[1].id)

# IMPLEMENTING THE Speak FUNCTION
def speak(audio):
    """this function takes text
       as an input and returns
       audio as an output"""
    engine.say(audio)
    engine.runAndWait()

# IMPLEMENTING THE TakeCommand FUNCTION
def takeCommand():
    """this function takes the microphone
    input and returns string as an output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"{query}")

        except:
            print("Please Say That Again")
            return "None"
        return query

# IMPLEMENTING THE WishMe FUNCTION
def WishMe():
    """this function greets us with respect to time"""
    hours = int(datetime.datetime.now().hour)

    if hours >= 0 and hours < 12:
        speak("Good Morning")

    elif hours >= 12 and hours <= 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("Hello Sir, i am prishi gaur, how can i help you")


# def sendEmail(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()
#     with open("password.txt", "r") as file:
#         password = file.read()
#         print(password)
#         server.login('nihkilgaur581@gmail.com', password)
#         server.sendmail('nikhilgaur581@gmail.com', to, content)
#     server.close()

if __name__ == '__main__':
    while True:
        WishMe()
        query = takeCommand().lower()

        # logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open_new("youtube.com/")

        elif "open google" in query:
            webbrowser.open_new("google.com/")

        elif "open stackoverflow" in query:
            webbrowser.open_new("stackoverflow.com/")

        elif "open github" in query:
            webbrowser.open_new("github.com/")

        elif "open colour game" in query:
            os.startfile("D:\\Virtual Desktop\\Nick Webpages\\Color Game\\colorgame.html")

        elif "the time" in query:
            speak(f"sir the time is {time.asctime(time.localtime(time.time()))}")


        # elif 'email' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "nikhilgaur3@rocketmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Sir, I am not able to send this email")

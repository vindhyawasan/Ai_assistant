import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speech(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speech("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour <=16:
        speech("Good afternoon")
        print("Good afternoon")
    else:
        speech("Good evening")
        print("Good evening")
    speech("I am Aditya sir how may i help you")
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lisgtening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said : {query}\n")
    except:
        print("Say that again please...")
        return None
    return query

def sendemail(to, content):
    try:
        sender_email = "examples12er@gmail.com"
        sender_password = "hbjc putx sbbd taym"  # Use environment variables instead

        # Setting up SMTP connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)

        # Formatting email
        # message = f"Subject: Automated Email\n\n{content}"
        server.sendmail(sender_email, to, content)

        # Closing connection
        server.close()
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    # speech("Shivam is a good boy")
    wishme()
    while True:
    # if 1:
        query = takecommand().lower()
        #logic for executing task based on query
        if "wikipedia" in query:
            try:
                speech("Searching Wikipedia")
                query = query.replace("wikipedia", "").strip()  # Remove 'wikipedia' and extra spaces

                if not query:
                    speech("Please specify a topic to search.")


                result = wikipedia.summary(query, sentences=2)  # Get summary
                speech("According to Wikipedia...")
                print(result)
                speech(result)
            except Exception:
                pass
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'start music' in query:
            music = "D:\\Music"
            song=os.listdir(music)
            print(song)
            r1=random.randint(0,80)
            print(r1)
            os.startfile(os.path.join(music,song[r1]))
        elif 'change music' in query:
            music = "D:\\Music"
            song = os.listdir(music)
            r2 = random.randint(0,80)
            print(r2)
            os.startfile(os.path.join(music,song[r2]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speech(f"The time is {time}")
            print(time)
        elif 'open visual studio' in query:
            open = "C:\\Users\\SHIVAM\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(open)
        if "send email" in query:
            try:
                speech("What should I say?")
                content = takecommand()
                to = "asingh128ve@gmail.com"  # Replace with recipient email
                sendemail(to, content)
            except Exception as e:
                print(e)
                speech("Sorry, I was unable to send the email.")
            
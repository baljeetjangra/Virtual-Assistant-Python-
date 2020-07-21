

import pyttsx3 #pip install pyttsx3 ,  It converts text to speech
import speech_recognition
import wikipedia # pip install wikipedia
import datetime
import random




def speak(text):
    engine = pyttsx3.init()
    #check the voices avilable
    voices = engine.getProperty('voices')
    #change the assiatant voice to voice with id 1(Zira's voice)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait() 

#When Assistant run. It wishes the user according to time. 
def wish_me():
    # Get the hour using date time module
    now = datetime.datetime.now().time().hour
    #compare hours to get the greeting time     
    if now > 0 and now < 12:
        greeting = 'Good Morning'
    elif now > 12 and now < 17:
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'
    #create a response to greet user
    response = f"{greeting} Sir, I'm Your Virtual Assistant. How May I Help You!"
    #speak function with argument response/text 
    speak(response)
    


def take_command():
    pass




if __name__ == "__main__":
    wish_me()

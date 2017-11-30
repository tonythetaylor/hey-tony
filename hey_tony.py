#!/usr/bin/env python3                                                                                
import speech_recognition as sr  
from datetime import datetime
import time
# from gtts import gTTS
from os import system
import os,sys

hey = "hey Tony"
hmm = "Humm!"
# get audio from the microphone                                                                       
r = sr.Recognizer()
                                                                                  
def getAudio():
    with sr.Microphone() as source:                                                                    
        print("Say 'Hey Tony' to activate or 'Goodbye' to exit: ")                                                                                   
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) == hey:
                user = system('echo $USER')
                hcihu = "How can I help you?"
                print(hcihu) 
                system('say '+ hcihu + '$USER') 
                audio = r.listen(source)
                return audio
            elif r.recognize_google(audio) == "goodbye":
                print("later")
                sys.exit(0)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def giveTime(audio):
    try:
        print("You said, " + r.recognize_google(audio))
        if r.recognize_google(audio) == "what time is it":
            ctime = time.strftime('%I:%M %p')
            telltime = "It is " + ctime
            system('say '+ telltime)
            print(telltime)
            moreHelp()
        else:
            moreHelp()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def moreHelp():
    with sr.Microphone() as source:
        try:
            system('say "Do you need more assistance?"')
            audio = r.listen(source)
            print(r.recognize_google(audio)) # for debugging
            if r.recognize_google(audio) == "yes":
                getAudio()
            elif r.recognize_google(audio) == "no":
                system('say Goodbye!')
                print("Goodbye!")
                sys.exit(0)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def main():
    audio = getAudio()
    giveTime(audio)

if __name__=="__main__":
    main()
#!/usr/bin/env python3                                                                                
import speech_recognition as sr  
from datetime import datetime
import time
from os import system
import os,sys

import requests
from bs4 import BeautifulSoup

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
                # user = system('echo $USER')
                hcihu = "How can I help you?"
                # print(hcihu) 
                # system('say '+ hcihu + '$USER') 
                system('say '+ hcihu) 
                audio = r.listen(source)
                return audio
            elif r.recognize_google(audio) == "goodbye":
                # print("later")
                sys.exit(0)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def giveTime(audio,period,short_desc):
    try:
        # print("You said, " + r.recognize_google(audio))
        if r.recognize_google(audio) == "what time is it":
            ctime = time.strftime('%I:%M %p')
            telltime = "It is " + ctime
            night = str(period) + " there will be a " + str(short_desc)
            system('say '+ telltime)
            if ctime > "05:00 PM" and ctime < "12:00 AM":
                system('say ' + night)
                # print(night)
            elif ctime > "12:00 AM" and ctime > "05:00 AM":
                system('say Isnt it past your bed time? ')
            elif ctime > "12:00 PM" and ctime < "05:00 PM":
                # system('say Isn\'t it past your bed time? ')
                print("midday")
            elif ctime > "05:00 AM" and ctime < "12:00 PM":
                print("good morning!")
            else:
            # print(telltime)
                print("It's too early to be up!")
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
            # print(r.recognize_google(audio)) # for debugging
            if r.recognize_google(audio) == "yes":
                getAudio()
            elif r.recognize_google(audio) == "no":
                system('say Goodbye!')
                # print("Goodbye!")
                sys.exit(0)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def getCurrentWeather():
    page = requests.get("http://forecast.weather.gov/MapClick.php?lat=39.20569490000014&lon=-76.6574066#.WYN0e9PyvBI")
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    period = tonight.find(class_="period-name").get_text()
    short_desc = tonight.find(class_="short-desc").get_text()
    index = short_desc.find('Showers')
    output_line = short_desc[:index] + ' of ' + short_desc[index:]
    short_desc = output_line
    # removed 'temp' until the degree symbol can be removed. Throws Unicode/ASCII error. 
    temp = tonight.find(class_="temp").get_text() 

    # night = period + "there will be a " + short_desc + " " + temp
    return period,short_desc

def main():
    audio = getAudio()
    period,short_desc = getCurrentWeather()
    giveTime(audio,period,short_desc)

if __name__=="__main__":
    main()
# Names: Daniel Calderon, Terra Fenton, Nancy Gomez

import speech_recognition as sr
import sys
import webbrowser
import os
import subprocess
from docx import Document
from docx.shared import Inches
r = sr.Recognizer()

# The microphone will be the source of our audio
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    # sets the threshold to a good value automatically.
    with m as source: r.adjust_for_ambient_noise(source)
    
    # Sets the sensitivity of the recognizer depending on the noise level of the room
    # (so louder values means there is a louder room)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print("You said {}".format(value).encode("utf-8"))
                #Google Website
                if ("chrome" in value or "Chrome" in value or "Google" in value or "google" in value ):
                    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com")
                elif ("apple" in value or "Apple" in value):
                        webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://apple.com")
				#Yahoo Website
                elif ("yahoo" in value or "Yahoo" in value) :
                    webbrowser.open("http://yahoo.com")
                #Disney Store
                elif ("Disney store" in value or "Disney" in value) :
                    webbrowser.open("http://www.disneystore.com")
                #NotePad
                elif (("word" in value) or ("text" in value)):
                    document = Document()
                    print("say whatever you need to say(if you wish to start please say START AGAIN PYTHON")
                    with m as source: audio = r.listen(source)
                    try:
                        value = r.recognize_google(audio)
                        if("Start again python" in value or "start again pythin" in value):
                            with m as source: audio = r.listen(source)
                            try:
                                value = r.recognize_google(audio)
                            except sr.UnknownValueError:
                                print("Didnt catch that")
                        else:
                            document.add_paragraph(value)
                        print("******************************")
                        print("Enter name of file")
                        print("******************************")
                        with m as source: audio = r.listen(source)
                        try:
                            value = r.recognize_google(audio)
                            print ("Path is "+ value+".docx")
                            
                            path = format(value).encode("utf-8")+".docx"
                            document.save(path)
                            open(path)
                        except sr.UnknownValueError:
                            print("Didnt catch that")
                            
                    except sr.UnknownValueError:
                            print("Oops! Didn't catch that")
                #Apple texting
                elif(("message" in value) or ("text message" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Messages.app"])
                #Steam
                elif(("Steam" in value) or ("steam" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Steam.app"])
                #Photo Both
                elif(("Booth" in value) or ("booth" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Photo Booth.app"])
                #Pictures
                elif(("Photo" in value) or ("photo" in value) or ("picture" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Photos.app "])
                #Skype
                elif(("Skype" in value) or ("skype" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Skype.app"])
                #iTunes
                elif(("eye Tunes" in value) or ("iTunes" in value) or ("Tunes" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/iTunes.app"])
                #Calculator
                elif(("calculator" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Calculator.app"])
                #Close Code
                elif(("close" in value) or ("Lowe's" in value)):
                    raise SystemExit
                    print "Goes here"
                #League
                elif (("LOL" in value) or ("League" in value) or ("League of Legends" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/League of Legends.app"])
       
        # if the value (sound) wasn't recognizable, print an error message
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        # if there is an error with the actual API, print an error message
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            
# this exception takes care of ending the program when the user enters Ctrl + C, doesn't give an error
except KeyboardInterrupt:
    pass

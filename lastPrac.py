"""
@author: Washington Mumbo Mirema
Innovation Day present
"""
import pyttsx3
import speech_recognition as sr
import datetime 
from datetime import date
import calendar
import time
import math
import os
import smtplib
import winsound
import pyautogui
import cv2
from tkinter import *
import tkinter.messagebox as message

global query
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def detect_face():
    cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)
        speak("Detecting face")
        print("Detecting face.....")
        time.sleep(4)      
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Please tell me how may I help you.")
    
def takeCommand():
    global query
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Visitor: {query}\n")
        
    except Exception as e:
        #print(e)     
        #print("Say that again please...")  
        speak('Say that again please...')
        return "None"    
    return query
        



if __name__ == "__main__":
    detect_face()
    wishMe()
    said = True
    while said:

        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'cancer' in query:
            speak('For cancer treatment, visit third floor')
 
        elif 'face' in query and ('detect' in query or 'identify' in query or 'point' in query or 'highlight' in query or 'focus' in query):
            speak('okay')
            detect_face()
                           
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            
        elif 'open' in query and 'music' in query:
            path = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(path)   
            
        elif 'quit' in query:
            speak('Ok, Thank you Sir.')
            said = False

        elif 'exit' in query:
            speak('Ok, Thank you Sir.')
            said = False
            
        elif 'stop' in query:
            speak('Ok, Thank you Sir.')
            said = False
            
        elif 'shutdown' in query or 'shut down' in query:
            speak('Ok, Thank you Sir.')
            said = False
            
        elif 'bye' in query:
            speak('Bye')
            said = False
        
        elif 'change' in query and 'you' in query and 'voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak("Here's another voice. Do you like this one?")
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('Great. I will keep using this voice.')
            elif 'n' in query:
                speak('Ok. I am back to male voice.')
                engine.setProperty('voice', voices[0].id)
            else:
                speak('Sorry, I am having problems understanding. I am back to male voice.')
                engine.setProperty('voice', voices[0].id)
       
        elif 'getting bore' in query:
            speak('then speak with me for sometime')
        elif 'i bore' in query:
            speak('Then speak with me for sometime.')
        elif 'i am bore' in query:
            speak('Then speak with me for sometime.')
  
        elif 'write' in query and ('I' in query or 'whatever' in query) and 'say' in query:
            speak('Ok sir I will write whatever you will say. Please put your cursor where I have to write.......Please Start speaking now sir.')
            query = takeCommand().lower()
            pyautogui.write(query) 
        elif 'your name' in query:
            speak('My name is AssistMe')
        elif 'who are you' in query:
            speak('I am AssistMe')
        elif ('repeat' in query and ('word' in query or 'sentence' in query or 'line' in query) and ('say' in query or 'tell' in query)) or ('repeat' in query and 'after' in query and ('me' in query or 'my' in query)):
            speak('yes sir, I will repeat your words starting from now')
            query = takeCommand().lower()
            speak(query)
            time.sleep(1)
 
        elif 'you communicate' in query:
            speak('Yes, I can communicate with you.')
        elif 'hear me' in query:
            speak('Yes sir, I can hear you.')
        elif 'you' in query and 'dance' in query:
            speak('No, I cannot dance.')
        elif 'tell' in query and 'joke' in query:
            speak("Ok, here's a joke")
            speak("'Write an essay on cricket', the teacher told the class. Chintu finishes his work in five minutes. The teacher is impressed, she asks chintu to read his essay aloud for everyone. Chintu reads,'The match is cancelled because of rain', hehehehe,haahaahaa,hehehehe,haahaahaa")

        
        elif 'day after tomorrow' in query or 'date after tomorrow' in query:
            td = datetime.date.today() + datetime.timedelta(days=2)
            print(td)
            speak(td)
        elif 'day before today' in query or 'date before today' in query or 'yesterday' in query or 'previous day' in query:
            td = datetime.date.today() + datetime.timedelta(days= -1)
            print(td)
            speak(td)
        elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
            td = datetime.date.today() + datetime.timedelta(days=1)
            print(td)
            speak(td)
        elif 'month' in query or ('current' in query and 'month' in query):
            current_date = date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            speak(f'Current month is {month}')
        elif 'date' in query or ('today' in query and 'date' in query) or 'what is today' in query or ('current' in query and 'date' in query):
            current_date = date.today()           
            print(f"Today's date is {current_date}")
            speak(f'Todays date is {current_date}')
            
        elif 'year' in query or ('current' in query and 'year' in query):
            current_date = date.today()
            m = current_date.year
            print(f'Current year is {m}')
            speak(f'Current year is {m}')
        elif 'sorry' in query:
            speak("It's ok sir")
        elif 'thank you' in query:
            speak('my pleasure')
        elif 'proud of you' in query:
            speak('Thank you sir')
 
        elif 'play' in query or 'turn on' in query and ('music' in query or 'song' in query) :
           try:
               music_dir = 'C:\\Users\\Admin\\Music\\Playlists'
               songs = os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir, songs[0]))
           except Exception as e:
               #print(e)
               speak('Sorry sir, I am not able to play music')
            
        elif (('open' in query or 'turn on' in query) and 'camera' in query) or (('click' in query or 'take' in query) and ('photo' in query or 'pic' in query)):
            speak("Opening camera")
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("Visitor")

            img_counter = 0
            speak('say click, to click photo.....and if you want to turn off the camera, say turn off the camera')

            while True:
                ret, frame = cam.read()
                if not ret:

                    speak('Cannot grab frame')
                    break
                cv2.imshow("Visitor", frame)

                query = takeCommand().lower()
                k = cv2.waitKey(1)
                
                if 'click' in query or ('take' in query and 'photo' in query):
                    speak('Be ready!...... 3.....2........1..........')
                    pyautogui.press('space')
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'escape' in query or 'off' in query or 'close' in query:
                    pyautogui.press('esc')
                    speak('Turning off the camera')
                    break
                elif k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
        
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'exit' in query or 'stop' in query or 'bye' in query:
                    speak('Please say, turn off the camera or press escape button before giving any other command')
                else:
                    speak('I did not understand what did you say or you entered a wrong key.')

            cam.release()

            cv2.destroyAllWindows()
            
            
        elif 'screenshot' in query:
            speak('After 2 seconds I will take screenshot')
            time.sleep(2)
            speak('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('Patient.png') 
            speak('The screenshot is saved as Patient.png')
        elif 'click' in query and 'start' in query:
            pyautogui.moveTo(10,1200)    
            pyautogui.click()
        elif ('open' in query or 'click' in query) and 'calendar' in query:
            pyautogui.moveTo(1800,1200)   
            pyautogui.click() 
        elif 'increase' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumeup') 
        elif 'decrease' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumedown')
        elif 'mute' in query:
            pyautogui.press('volumemute')
        elif 'search' in query and ('bottom' in query or 'pc' in query or 'laptop' in query or 'app' in query):
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            speak('What do you want to search?')
            query = takeCommand().lower() 

        elif 'me the answer' in query:
            speak('Yes, I will try my best to answer you.')
        elif 'me answer' in query or ('answer' in query and 'question' in query):
            speak('Yes, I will try my best to answer you.')
        elif 'can you' in query or 'could you' in query:
            speak('I will try my best if I can do that.')
        elif 'do you' in query:
            speak('I will try my best if I can do that.')
        elif 'truth' in query:
            speak('I always speak truth. I never lie.')
        elif 'true' in query:
            speak('I always speak truth. I never lie.')        
        elif 'lying' in query:
            speak('I always speak truth. I never lie.')
        elif 'liar' in query:
            speak('I always speak truth. I never lie.')    
        elif 'doubt' in query:
            speak('I will try my best if I can clear your doubt.')
            
        elif 'hey' in query:
            speak('hello')
        elif 'hai' in query:
            speak('hello')
        elif 'hay' in query:
            speak('hello')
        elif 'hi' in query:
            speak('hii')
        elif 'hello' in query:
            speak('hello!')

        elif 'shut up' in query:
            speak("I'm sorry sir")
        elif 'nice' in query:
            speak('Thank you sir')
        elif 'good' in query or 'wonderful' in query or 'great' in query:
            speak('Thank you sir')
        elif 'excellent' in query:
            speak('Thank you sir')
        elif 'ok' in query:
            speak('Hmmmmmm')
        

        elif 'AssistMe' in query:
            speak('yes')

            
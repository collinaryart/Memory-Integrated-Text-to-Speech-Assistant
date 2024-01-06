import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia 

def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listening')
		

		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		try:
			print("Recognizing")
			
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the assistant
	engine.say(audio) 
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	day = datetime.datetime.today().weekday() + 1
	
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	time = str(datetime.datetime.now())
	
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes") 

def Hello():
	
	speak("hello sir I am MITSA, your desktop Assistant. How may I help you")


def Take_query():

	Hello()
	
	while(True):
		query = takeCommand().lower()
		if "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("goodbye sir, have a good day!")
			exit()
		
		elif "from wikipedia" in query:
			

			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am MITSA. Your desktop Assistant")

if __name__ == '__main__':
	
	Take_query()

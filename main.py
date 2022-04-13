import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)

def speak(audio):
	print(audio)
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)

	if hour>=0 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")

	speak("How may I help you?")

def takeCommand():
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold=1
		r.energy_threshold=300
		audio=r.listen(source)

	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language='en-in')
		print(f"You said: {query}\n")
	
	except Exception as e:
		return ""

	return query

wishMe()
while True:
	query=takeCommand().lower()
	if 'alexa' in query:
		query=query.replace("alexa","")

		if 'stop' in query or 'quit' in query or 'exit' in query:
			speak("Thank you. Have a nice day.")
			break

		elif 'open' in query or 'start' in query:
			if 'youtube' in query:
				webbrowser.open('m.youtube.com')
			elif 'google' in query:
				webbrowser.open('www.google.com')

		elif 'wish me' in query:
			wishMe()

		elif 'who is adarsh kumar' in query:
			ans="Adarsh Kumar, brother of Ayush Kumar, is a nine year old very smart boy studying in Rajendra Vidyaalaya. He listens to everyone and studies daily."
			speak(ans)

		elif 'the time' in query:
			Time=datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {Time}")

		elif 'the date' in query:
			date=datetime.datetime.now()
			yr=date.year
			mt=date.month
			dt=date.day
			MONTH=["January","February","March","April","May","June","July","August","September","October","November","December"]
			DATE=f"{dt} {MONTH[mt-1]} {yr}"
			speak(DATE)

		else:
			if 'tell me something about' in query:
				query=query.replace("tell me something about","")
			elif 'what is' in query:
				query=query.replace("what is","")
			print(query)
			try:
				results=wikipedia.summary(query,sentences=2)
				speak("Searching Wikipedia...")
				speak("According to wikipedia...")
				speak(results)
			except Exception as e:
				speak("Sorry, I did not get that.")

	time.sleep(3)
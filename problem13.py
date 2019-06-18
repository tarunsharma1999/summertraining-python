#!/usr/bin/python3
import pyttsx3
import datetime
def echotext():
	
	sound_var=pyttsx3.init()
	sound_var.setProperty('rate',150)
	sound_var.say("Enter Your Name:")
	sound_var.runAndWait()
	sound_var.say(input())
	sound_var.runAndWait()
	
	currenttime=datetime.datetime.now().hour
	if currenttime<12:
		sound_var.say("Good Morning")
		sound_var.runAndWait()
	elif currenttime>12 and currenttime <16:
                sound_var.say("Good Afternoon")
                sound_var.runAndWait()
	elif currenttime>16 and currenttime <21:
                sound_var.say("Good Evening")
                sound_var.runAndWait()
	else:
                sound_var.say("Good Night")
                sound_var.runAndWait()

echotext()

def num():
	voice=pyttsx3.init()
	voice.setProperty('rate',150)
	voice.say("Enter How many numbers you need:")
	voice.runAndWait()
	n=int(input())
	voice.say("Enter numbers:")
	voice.runAndWait()
	s=[]
	for i in range(0,n):
		l=int(input())
		s.append(l)
	total=0
	for  i in s:
		total=total+i
	voice.say("total is:")
	voice.runAndWait()
	voice.say(total)
	voice.runAndWait()
	voice.say("sort?")
	voice.runAndWait()
	choice=input()
	if choice == 'yes' :
		voice.say("Numbers After Sorting:")
		voice.say(sorted(s))
		voice.runAndWait()
		print(sorted(s))

num()
import os
voice=pyttsx3.init()
voice.say("modules used:")
os.system("pip3 list")

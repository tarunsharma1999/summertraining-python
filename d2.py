#comment
#inital commits
import subprocess
import time
import webbrowser 
option='''
enter 1 to vlc
enter 2 to search on google
enter 3 to play youtube
enter 4 5 for time
'''
choice = input()
if choice == '4' :
	print(time.ctime())
elif choice == '1' :
	subprocess.getouput('cls')
elif choice == '2' :
	print("Enter something to search:")
	usrinput=input()
	webbrowser.open_new_tab('https://www.google.com./search?q='+usrinput)

''' top5 url store in a list and open them with delay of 5'''


from googlesearch import search
import webbrowser
import pyqrcode

Tosearch=input("Enter something to search on Google:")
li=[]
li1=[]
for i in search(Tosearch,tld='com',lang='en',num=2,start=0,stop=4,pause=0):
	li.append(i)
for i in range(len(li)):
	url=pyqrcode.create(li[i])
	url.svg("search{}.png".format(i+1),scale=16)


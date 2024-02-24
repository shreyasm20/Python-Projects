#this program works on mac
'''
import os
print("Welcome to Robospeak. \nCreated by Shreyas.")
a=input("Enter text that you want to pronounce: ")
command =(f"echo{a}")
os.system(command)
'''
#for windows
import win32com.client as win 
voice= win.Dispatch("SAPI.Spvoice")
print("Welcome to RoboSpeak.\n Created by Shreyas")
while True:
    a=input("Enter the text you want to pronounce: ")
    voice.Speak(a)
    if(a == "quit" or a=="Quit" or a =="exit" or a == "Exit"):
        break

import time
import win32com.client as win
voice= win.Dispatch("SAPI.Spvoice")
timestamp= time.strftime("%H:%M:%S")
print("Current time:",timestamp)
hour= int(time.strftime("%H"))
if(hour>=4 and hour<12):
    a=("Good Morning")
    print(a)
    voice.Speak(a)
elif(hour>=12 and hour<17):
    b=("Good afternoon")
    print(b)
    voice.Speak(b)
elif(hour>=17 and hour<21):
    c =("Good evening")
    print(c)
    voice.Speak(c)
else:
    d=("Good night")
    print(d)
    voice.Speak(d)

    


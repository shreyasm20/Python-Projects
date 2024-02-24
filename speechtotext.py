import pyttsx3
import speech_recognition as sr
import pyaudio


recognizer = sr.Recognizer()
print("The voice recognizer is active now!")

while True:
    
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
            audio = recognizer.listen(mic)

            text= recognizer.recognize_google(audio)
            text = text.lower()
        
            print(f"Your audio to text output is: \n {text}",)
            break


    except sr.UnknownValueError:

        print("Unknownerror")
    
    break 
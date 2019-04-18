import speech_recognition as ar
r = ar.Recognizer()

with ar.Microphone() as source:
    print("Say Anything! dude!!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you are say that: {0}".format(text))
    except:
        print("Your voice iz not clear")
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        Audio = r.listen(source)

    try:
        voice_data=""
        voice_data= r.recognize_google(Audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("requestError")

#speech_to_text()
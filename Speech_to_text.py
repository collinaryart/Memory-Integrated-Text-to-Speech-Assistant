import speech_recognition as sr

def speech_to_text():
    """
    Converts speech to text using the microphone.
    """
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)  # Listen to the audio via microphone
        
        try:
            # Using Google's speech recognition to convert audio to text
            text = r.recognize_google(audio)
            print(f"You said : {text}")
        except:
            print("Sorry could not recognize your voice")

speech_to_text()  # Call the function to start speech recognition

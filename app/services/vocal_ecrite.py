import speech_recognition as sr

def listen_and_recognize():
    # Créer l'objet pour la reconnaissance vocale
    recognizer = sr.Recognizer()

    # Utiliser le micro pour capturer l'audio
    with sr.Microphone() as source:
        print("Attendez un moment, réglage du bruit ambiant...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustement du bruit ambiant
        print("Parlez maintenant...")
        audio = recognizer.listen(source)  # Enregistrer l'audio

    try:
        # Reconnaissance vocale via Google Web Speech API
        command = recognizer.recognize_google(audio, language='fr-FR')  # Corriger "langage" -> "language"
        print(f"Vous avez dit : {command}")
        return command
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit.")
        return None
    except sr.RequestError as e:
        print(f"Erreur avec le service de reconnaissance vocale : {e}")
        return None

if __name__ == "__main__":
    listen_and_recognize()

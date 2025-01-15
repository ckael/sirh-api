#pip install googletrans==4.0.0
from googletrans import Translator, LANGUAGES
import asyncio


def translate(text, dest_language):
    translator = Translator()
    if dest_language not in LANGUAGES:
        return "Langue invalide"
    try:
        translation = asyncio.run(translator.translate(text, dest=dest_language))
        return translation.text
    except Exception as e:
        return f"Erreur lors de la traduction : {e}"


#if __name__ == '__main__':
#   text_to_translate = input("Saisir votre texte : ")
#    print("Langues disponibles :")
#    for lang_code, lang_name in LANGUAGES.items():
#        print(f"{lang_code}: {lang_name}")

#    destination_language = input("Traduire en (code langue, ex: 'fr' pour français) : ")

#    if destination_language not in LANGUAGES:
#        print("Langue invalide. Veuillez entrer un code langue valide.")
#    else:
#        translated_text = translate_text(text_to_translate, destination_language)
#        print(f"Résultat : {translated_text}")

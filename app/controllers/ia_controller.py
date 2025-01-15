from flask import request, jsonify
from app.services.correction_texte import correction
from app.services.generate_qrcode import generate
from app.services.resume import resume
from app.services.translation import translate
from app.services.speech_to_text import listen_and_recognize

def text_correction():
    text = request.form.get('texte')
    texte_corriger = correction(text)
    print(texte_corriger)
    return jsonify({"texte":f"{texte_corriger}"}),200

def generate_qrcode():
    link = request.form.get("link")
    name = request.form.get("name")
    path_qr_code = generate(link,name)
    return jsonify({"message":"Votre qr code est generer",
                    "path":f"{path_qr_code}"}),200

def resume_text():
    text = request.form.get('texte')
    resume_texte = resume(text)
    print(resume_texte)
    return jsonify({"resume":f"{resume_texte}"}),200

def translate_text():
    text = request.form.get('texte')
    destination_language = request.form.get('langue')
    translated_text = translate(text,destination_language)
    print(translated_text)
    return jsonify({"translated_text":f"{translated_text}"}),200

def listen():
    audio_file = request.files.get('audio')
    recognized_text = listen_and_recognize(audio_file)
    print(recognized_text)
    return jsonify({"recognized_text":f"{recognized_text}"}),200
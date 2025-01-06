from flask import jsonify, request
from app.services.face import reconnaissance

def recognize():

    image = request.files.get('image')

    if image is None :
        return jsonify({"message":"Aucun image envoyer"}),400
    if reconnaissance(image) :
        return jsonify({"message":"Utilisateur valider"}),200
    else :
        return jsonify({"message":"Utilisateur non trouver"}),404 
    
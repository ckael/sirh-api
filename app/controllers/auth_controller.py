from flask import jsonify, request
from app.services.face import reconnaissance
from flask_cors import cross_origin

@cross_origin()
def recognize():

    image = request.files.get('image')

    if image is None :
        print("pas d'image")
        return jsonify({"message":"Aucun image envoyer"}),400
    try:
        if reconnaissance(image) is True:
            print("image identique")
            return jsonify({"message":"Utilisateur valider","status":True}),200
        else :
            print("image non identique")
            return jsonify({"message":"Utilisateur non trouver","status":False}),201
    except Exception as e:
        return jsonify({"message":f"{e}","status":False}),500


    
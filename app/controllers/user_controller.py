from flask import jsonify, request,current_app
from app.models.users import User
from app import db
import json
 
def getAll():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])
    
 
def addUser():
    data = request.form.get('data')
    file = request.files.get('file')

    if data:
        if file:
            try:
                data = json.loads(data)
                username = data.get('username')
                email = data.get('email')
                password = data.get('password')
            except json.JSONDecodeError:
                return jsonify({"error": "Format JSON invalide"}), 400
            
            filename = file.filename
            image = current_app.config.get('UPLOADED_PHOTOS_DEST') +'\\'+ filename
            file.save(image)
            u = User(username=username, email=email, password=password, image=image)
            db.session.add(u)
            db.session.commit()
            return jsonify({"message": "Utilisateur ajouté avec succès"}), 201
        else:
            return jsonify({"error": "Fichier  manquants"}), 400
    else:
        return jsonify({"error": "Données manquantes"}), 400
from flask import jsonify, request, current_app
from app.models.users import User
from app import db
from flask_uploads import UploadSet, configure_uploads, IMAGES


class UserController():
    
    def getAll(self):
        users = User.query.all()
        return jsonify([user.serialize() for user in users])
    
    def addUser(self):
        data = request.get_json()

        if len(data) == 0:
            return jsonify({"error":"User not found"})
        
        data = data[0]
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        image = "../public/img/pic.jpg"
        u = User(username=username, email=email, password=password,image=image)
        db.session.add(u)
        db.session.commit()
        return jsonify("Utilisateur ajouter avec success"), 201
    
    def upload(self):
        if 'file' in request.files:
            filename = self.photos.save(request.files['file'])
            return jsonify({"message": "File successfully uploaded", "filename": filename}), 200
        return jsonify({"error": "No file part in the request"}), 400


        
    

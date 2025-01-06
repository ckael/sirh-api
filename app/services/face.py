import face_recognition

def reconnaissance(img_path):
    try :

        img = "app/public/img/pic2.jpg"

        image = face_recognition.load_image_file(img)

        img_to_recognize = face_recognition.load_image_file(img_path)

        # recherche et encodage
        face_encodings = face_recognition.face_encodings(image)[0]

        img_to_reconize_encodings = face_recognition.face_encodings(img_to_recognize)[0]

        # creation fenetre resultat

        compare = face_recognition.compare_faces([face_encodings], img_to_reconize_encodings)

        if compare[0]:
            label = True
        else:
            label = False

        return label
    except Exception as e :
        print(f"Erreur lors du comparaison : {e}")
import face_recognition


def compare_faces(image2_path):
    try:

        # Charger l'image avec PIL
        image_base = face_recognition.load_image_file("../puclic/pic2.jpg")
        image_test = face_recognition.load_image_file(image2_path)
        print("success")
        # Encoder les visages
        encodings1 = face_recognition.face_encodings(image_base)[0]
        encodings2 = face_recognition.face_encodings(image_test)[0]
        print("success")

        # Comparer les visages (prend le premier visage détecté dans chaque image)
        match = face_recognition.compare_faces([encodings1], encodings2)
        distance = face_recognition.face_distance([encodings1], encodings2)[0]

        # Afficher le résultat
        if match[0]:
            print(f"Les visages correspondent avec une distance de {distance:.2f}")
        else:
            print(f"Les visages ne correspondent pas. Distance : {distance:.2f}")

    except Exception as e:
        print(f"Erreur lors de la comparaison : {e}")

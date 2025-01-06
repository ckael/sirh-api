#pip install qrcode[pil]
import qrcode


# Texte à inclure dans le QR Code
source = "Rivo Andriamifidy"

# Initialisation de l'objet QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajouter les données au QR Code
qr.add_data(source)
qr.make(fit=True)

# Générer l'image du QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarder l'image
img.save("image.png")

print("Scanner ici: 'image.png'")

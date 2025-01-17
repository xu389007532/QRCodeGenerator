import qrcode
from PIL import Image
face=Image.open("CH-Kreuz_7mm.png")
qr = qrcode.QRCode(
    version=6,

    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=35,
    border=4,
)
qrcode.QRCode()
# qr.add_data("BCD\n002\n2\nSCT\n\n"+"François D'"+"Alsace S.A.\nFR1420041010050500013M02606\nEUR12.3\n\n\nClient:Marie Louise La Lune\n\n")
# qr.add_data("BCD\n001\n1\nSCT\nBHBLDEHHXXX\nFranz Mustermänn\nDE71110220330123456789\nEUR12.3\nGDDS\nRF18539007547034\n\n\n")
# qr.add_data("BCD\r\n002\r\n2\r\nSCT\r\nBHBLDEHHXXX\r\nFranz Mustermänn\r\nDE71110220330123456789\r\nEUR12.3\r\nGDDS\r\nRF18539007547034\r\n\r\n\r\n")
qr.add_data("BCD\r\n001\r\n2\r\nSCT\r\nGIBAATWWXXX\r\nROTE NASEN Clowndoctors, 1170 Wien\r\nAT822011182224146701\r\n0.01\r\n\r\n209132825760")
qr.make(fit=True)
img_qr_big=qr.make_image(fill_color="black", back_color="white")
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
# img_qr_big.paste(face, pos)

img_qr_big.save("some_file46v6.png")
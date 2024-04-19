import qrcode
from PIL import Image
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/qrCode', methods=['POST'])
def generateQrCode():
    face = Image.open('adway.png')

    qr_big = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=10
    )
    qr_big.add_data(request.args.get('supportUrl'))
    qr_big.make()
    img_qr_big = qr_big.make_image(fill_color="gray", back_color="white")

    pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

    img_qr_big.paste(face, pos)
    img_qr_big.save('abhijeet.png')

    return "Successfully generated QR Code !!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
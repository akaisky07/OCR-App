import io
from PIL import Image
import pytesseract
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/image_upload", methods=["POST"])
def image_upload():
    # Get the image from the request
    image = request.files["image"].read()
    # Convert the image to a PIL Image object
    image = Image.open(io.BytesIO(image))
    # Use Tesseract-OCR to extract text from the image
    text = pytesseract.image_to_string(image)
    # Return the text as a response to the client
    return jsonify(text=text)

if __name__ == "__main__":
    app.run(debug=True)


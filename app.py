from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
import tensorflow_image_classifier


#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods = ['POST'])
def upload():

    f = request.files['picture.jpg']
    f.save('picture.jpg')
    
    toReturn = tensorflow_image_classifier.imageClassifier('picture.jpg')
    print(toReturn)
    if len(toReturn) == 0:
        return 'Unknown Object'
    toReturnString = ""
    if len(toReturn) == 1:
        return toReturn[0]
    for i in range(0, len(toReturn)):
        if (i == len(toReturn)-1):
            toReturnString+=" and a "+toReturn[i]
        else:
            toReturnString+=toReturn[i]+", a "
    return toReturnString
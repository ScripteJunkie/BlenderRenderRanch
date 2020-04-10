from flask import Flask
import renderexecute as re
import sessionkeygenerator as sk
import platform

UPLOAD_FOLDER = ''
filename = ''

if (platform.system() == "Linux"):
    UPLOAD_FOLDER = "/home/machine01/BlenderRenderRanch/RenderBarn/"
else:
    UPLOAD_FOLDER = "C:/BlenderRenderRanch/RenderBarn/"


app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

import os
#import magic
import urllib.request
#from urllib import request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['blend'])
print(re.folder)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			re.render()
			return redirect('/')
		else:
			flash('Please upload .blend')
			return redirect(request.url)

#@app.route('/render')
#def postrender():


if __name__ == "__main__":
    app.run(host='192.168.2.155')
    #app.run()

#@app.route('/')
#def home():
#    return render("welcome.html")

#@app.route('/render')
#def render():
#    return "Upload .blend"

#if __name__ == "__main__":
#    app.run(debug=True)

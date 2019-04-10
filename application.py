from flask import Flask, render_template, request, jsonify
import os
from PIL import Image

app = Flask(__name__)

postReqParameter = 'file'
invalidReq = "The inputs supplied are not valid"

def isCorrectImage(file):
	ext = file.split('.')[-1]
	extenstionList = ['jpg', 'png', 'jpeg']
	if ext in extenstionList:
		return True
	else:
		return False

@app.route("/")
def index():
	return(render_template("index.html"))

@app.route("/api",methods=['POST'])
def api():
	if postReqParameter not in request.files:
		return jsonify(invalidReq)
	image = request.files[postReqParameter]
	request.files[postReqParameter].save('/tmp/{}'.format(image.filename))
	
	if not isCorrectImage(image.filename):
		return jsonify(invalidReq)

	imgName = image.filename
	width, height = Image.open('/tmp/{}'.format(imgName)).size
	resolution = "{} x {}".format(width, height)
	imgLength = os.stat('/tmp/{}'.format(imgName)).st_size
	imgLength /= 1024*1024
	imgLength = "{0:.3f} MB".format(imgLength)

	return jsonify(image_name=imgName, image_resolution=resolution, image_size=imgLength)

if __name__ == "__main__":
	app.run()
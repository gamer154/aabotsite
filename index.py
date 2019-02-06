import requests
import time

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return  "Hello there my friend !!"
	
@app.route('/home', methods=['GET'])
def home():
    return  render_template("home.html")

	
if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
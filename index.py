import requests
import time
import random

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
    triggerwelcome()
    return  render_template("home.html")

def triggerwelcome():
    #seId = random.randint(1,100)*50
	triggerurl = "https://dialogflow.googleapis.com/v2/projects/aachatbot-81afa/agent/sessions/aa551b50-44c2-a6f8-9f46-7ff1cd7e3856:detectIntent"
	data = {"queryInput":{"text":{"text":"Hello","languageCode":"en"}},"queryParams":{"timeZone":"America/Chicago"}}
    data_json = json.dumps(data)
    headers = {'Content-Type':'application/json', 'Authorization':'Bearer ya29.c.ElqoBq8wpD0R2ygLBssKhbKlR7L87_7JIpm15ukZ3ruW1AXyTGA3mZMORaIjYc1nZewvTXiyFYVZAr3wqYcX6Za_GsNGrNZgtJ4J290rnqk5VdOLteHh-fBhryk'}
    response = requests.post(triggerurl, data=data_json, headers=headers)
	
if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
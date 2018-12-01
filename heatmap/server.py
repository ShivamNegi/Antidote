from flask import Flask, render_template
import requests

import sys

API_KEY = "b3b79ab67a63ccd0bac9020dd0bd4789b57087e1"
app = Flask(__name__)

headers = {'RECEIPTHERO_APIKEY': 'b3b79ab67a63ccd0bac9020dd0bd4789b57087e1'}

def _url(path):
    return 'https://api.dev.receipthero.io' + path

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/v1/<event>')
def event_handler(event):
	if event == 'Malaria':
		with open('events/sample.json', 'r') as container:
			data = container.read()
	elif event == 'TB':
		with open('events/sample2.json', 'r') as container:
			data = container.read()
	elif event == 'Jaundice':
		with open('events/sample2.json', 'r') as container:
			data = container.read()
	elif event == 'Diarrhoea':
		with open('events/sample2.json', 'r') as container:
			data = container.read()

	return data

@app.route('/api/v1/users/', methods = ['GET'])
def get_users():
	data = requests.get(_url('/api/v1/users/'), headers=headers)
	print(data.content, file=sys.stdout)
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

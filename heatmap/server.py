from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/v1/<event>')
def event_handler(event):
	if event == 'small':
		with open('events/sample.json', 'r') as container:
			data = container.read()
	else:
		with open('events/sample2.json', 'r') as container:
			data = container.read()

	return data

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
	flag = "flag{c0mpany_ph0ne}"
	return render_template('index.html', flag=flag)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)

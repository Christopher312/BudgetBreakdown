from flask import render_template, Flask, request, json, send_from_directory
import os
app = Flask(__name__, static_folder='./static')

@app.route('/')
def home():
    #return 'Index page'
    #root_dir = os.path.dirname(os.getcwd())
    #return send_from_directory(os.path.join(root_dir, 'static', 'js'), 'index.html')
    return render_template("index.html")

@app.route('/stategovt')
def stgov():
	return render_template("stategovt.html")

@app.route('/fedgovt')
def fedgov():
	return render_template('fedgovt.html')

@app.route('/colleges')
def colleges():
	return render_template('colleges.html')

@app.route('/charity')
def charity():
	return render_template('charity.html')

if __name__ == "__main__":
	app.run()
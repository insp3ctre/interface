from flask import Flask
from flask import request, render_template, redirect

import database as db


app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/interface')
def interface():
	return render_template("interface.html")


@app.route('/callback')
def callback():
	return render_template("")

@app.route('/nametoid')
def nametoid(methods = ['POST']):
	return "unimplemented"
	
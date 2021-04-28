from flask import Flask
from flask import request, render_template, redirect
from blt_funcx_toolkit.execution import run_console_cmd

import database as db


app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/interface', methods=['GET'])
def interface():
	if request.args.get('output') != None:
		blt_output = request.args['output']
	elif request.args.get('command'):
		return run_console_cmd(request.args['command'])

	else:
		blt_output = ""
	return render_template("interface.html", console_cmd=blt_output, location="/interface")


@app.route('/callback')
def callback():
	return render_template("")

@app.route('/nametoid')
def nametoid(methods = ['POST']):
	return "unimplemented"
	
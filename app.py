from flask import Flask, request, render_template, redirect, session, url_for
from blt_funcx_toolkit.execution import run_console_cmd
from flask.json import jsonify
from requests_oauthlib import OAuth2Session

import database as db
import os

app = Flask(__name__)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
app.secret_key = os.urandom(24)
app.run(debug=True)

client_id = "9c220ee646e003590a72"
client_secret = "473d66990c684b2caa0ad66885c80169bfe26812"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

@app.route('/')
@app.route('/login')
def login():
    github = OAuth2Session(client_id)
    authorization_url, currentstate = github.authorization_url(authorization_base_url)
    session['oauth_state'] = currentstate
    return redirect(authorization_url)

@app.route('/interface', methods=['GET'])
def interface():
    if session.get("oauth_token") != None:
        github = OAuth2Session(client_id, token=session['oauth_token'])
        dict_response = github.get('https://api.github.com/user').json()
        name = dict_response['name']
        if request.args.get('output') != None:
            blt_output = request.args['output']
        elif request.args.get('command'):
            return run_console_cmd(request.args['command'])

        else:
            blt_output = ""
        return render_template("interface.html", console_cmd=blt_output, username=name, location="/interface")
    else:
        return "You are not logged in"


@app.route('/callback')
def callback():
    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)
    session['oauth_token'] = token
    return redirect(url_for('interface'))

@app.route('/profile')
def nametoid(methods = ['GET']):
    github = OAuth2Session(client_id, token=session['oauth_token'])
    dict_response = github.get('https://api.github.com/user').json()
    return f"Name: {dict_response['name']}"
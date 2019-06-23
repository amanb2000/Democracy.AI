from functools import wraps
from flask import Flask, g, session, redirect, url_for, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Add Key for security things
app.secret_key = app.config['SECRET_KEY']
# Connection
mysql = MySQL()
mysql.init_app(app)

# Add Wraps
def login_required(f):
	@wraps(f)
	def declaration_function(*args, **kwargs):
		if get_user() is None:
			return redirect("/login")
		return f(*args, **kwargs)
	return declaration_function


# Add Contexts
def get_conn():
    g.conn = mysql.get_db()
    return g.conn

class User:

	def __init__(self, userid, username, email):
		self.id = userid
		self.username = username
		self.email = email

def add_user(data):
	session['user'] = User(data[0], data[1], data[2]).__dict__
	return session['user']

def get_user():
	if 'user' in session:
		return session['user']
	return None

from di import views, scripts, models

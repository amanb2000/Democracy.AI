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

# Add Contexts
def get_conn():
    g.conn = mysql.get_db()
    return g.conn

from di import views, scripts

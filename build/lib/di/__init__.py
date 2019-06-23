from functools import wraps
from flask import Flask, g, session, redirect, url_for, request, render_template
import pyodbc

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Add Key for security things

# Connection
sql = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+app.config.get('SQL_HOST')+';DATABASE='+app.config.get('SQL_DB')+';UID='+app.config.get('SQL_USER')+';PWD='+app.config.get('SQL_PASSWORD'))

# Add Contexts
def get_conn():
    g.conn = sql
    return g.conn

from di import views, scripts

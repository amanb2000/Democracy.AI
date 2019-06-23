from di import app, get_conn, get_user, add_user, login_required
from flask import request
from flask_bcrypt import generate_password_hash, check_password_hash
from uuid import uuid1
import os

@app.route("/addUser", methods=['POST'])
def register_user():
	# Get DB
	cursor = get_conn().cursor()
	# Build query
	query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
	cursor.execute(query, (request.form['user'], generate_password_hash(request.form['pass']), request.form['email']))
	usr = cursor.lastrowid
	cursor.execute("SELECT user_id, username, email FROM users WHERE user_id = %s LIMIT 1", (usr))
	add_user(cursor.fetchall()[0])
	get_conn().commit()
	return ""

@app.route("/loginUser", methods=['POST'])
def login_user():
	# Get DB
	cursor = get_conn().cursor()
	# Build query
	query = "SELECT user_id, password FROM users WHERE username = %s LIMIT 1"
	cursor.execute(query, (request.form['user']))
	usr = cursor.fetchall()[0]
	if (check_password_hash(usr[1], request.form['pass'])):
		query = "SELECT user_id, username, email FROM users WHERE user_id = %s LIMIT 1"
		cursor.execute(query, (usr[0]))
		add_user(cursor.fetchall()[0])
		return "0"
	return "-1"

@app.route("/downloadML", methods=['POST'])
def download_bigboi():
	id = request.form['id']
	return "no can do, soz"

@app.route("/voteML", methods=['POST'])
def vote_boi():
	id = request.form['id']
	voteVal = request.form['value']
	query = "INSERT INTO posts_votes (voteColumn) VALUES (%s) WHERE post_id = %s"
	cursor.execute(query, (value, id))
	# INSERT INTO TABLENAME (COLUMN1, COLUMN2, COLUMN3) VALUES (%s, %s, %s)
	return "Vote kinda received :)"

@app.route("/bookmarkML", methods=['POST'])
def bookmarky_boi():
	query = "INSERT INTO " # fill in when table is ready
	return "Added, but not really :/"

@app.route("/reportML", methods=['POST'])
def reporty_boi():
	id = request.form['id']
	report = request.form['report_body'] # TODO: Implement this
	return "Not ready yet, bro"

@app.route("/addAlgoFile", methods=['POST'])
def add_algorithm():
	file = request.files['script']
	filename = str(uuid1()) + "_" + file.filename
	pt = os.path.join(app.config['ALGOS_FOLDER'], filename)
	file.save(pt)
	return pt

@login_required
@app.route("/addAlgoData", methods=['POST'])
def add_algorithm_data():
	# Get DB
	cursor = get_conn().cursor()
	# Insert post
	query = "INSERT INTO posts (title, descript, img, algo, added_by) VALUES (%s, %s, %s, %s, %s)"
	cursor.execute(query, (request.form['title'], request.form['description'], request.form['picUrl'], request.form['filePath'], get_user()['id']))
	get_conn().commit()
	return ""

from di import app
from flask import request

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
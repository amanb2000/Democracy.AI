from di import app
from flask import request

@app.route("/downloadML", methods=['POST'])
def download_bigboi():
	id = request.form['id']


	return "no can do, soz"

@app.route("/voteML", methods=['POST'])
def vote_boi():
	id = rquest.form['id']
	voteVal = request.form['']
	query = "INSERT INTO posts_votes (voteColumn) VALUES (%s)"
	cursor.execute(query, ())
	# INSERT INTO TABLENAME (COLUMN1, COLUMN2, COLUMN3) VALUES (%s, %s, %s)
	return "Vote kinda received :)"

@app.route("/bookmarkML", methods=['POST'])
def bookmarky_boi():
	query = "INSERT INTO "
	return "Added, but not really :/"

@app.route("/reportML", methods=['POST'])
def reporty_boi():
	return "Big not ready yet, mah b"

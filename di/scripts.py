from di import app
from flask import request

@app.route("/downloadML", methods=['POST'])
def download_bigboi():
    return "no can do, soz"

@app.route("/voteML", methods=['POST'])
def vote_boi():
    return "Vote kinda received :)"

@app.route("/bookmarkML", methods=['POST'])
def bookmarky_boi():
    return "Added, but not really :/"

@app.route("/reportML", methods=['POST'])
def reporty_boi():
    return "Big not ready yet, mah b"

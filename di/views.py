from di import app, get_conn
from flask import render_template

@app.route("/")
def instantiate_home():
    # Get DB
    cursor = get_conn().cursor()
    # Make request
    cursor.execute("SELECT ")
    return render_template("schema1.html",
        learns=cursor.fetchall()
    )

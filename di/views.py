from di import app, get_conn
from flask import render_template

@app.route("/")
def instantiate_home():
    # Get DB
    cursor = get_conn().cursor()
    # Make request
    query = "SELECT post_id, title, descript, img, username FROM posts JOIN users ON users.user_id = posts.added_by FROM posts"
    # SELECT COLUMN1, COLUMN2 FROM TABLENAME
    cursor.execute(query)
    return render_template("schema1.html",
        learns=cursor.fetchall()
    )

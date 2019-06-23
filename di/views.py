from di import app, get_conn, login_required
from flask import render_template

@app.route("/")
def instantiate_home():
    # Get DB
    cursor = get_conn().cursor()
    # Make request
    query = '''SELECT post_id, title, descript, img, username FROM posts 
    			JOIN users ON users.user_id = posts.added_by'''
    # SELECT COLUMN1, COLUMN2 FROM TABLENAME
    cursor.execute(query)
    return render_template("schema1.html",
        learns=cursor.fetchall()
    )

@app.route("/login")
def instantiate_login():
	return render_template("login/login.html")

@app.route("/register")
def instantiate_register():
	return render_template("login/register.html")

@app.route("/create")
@login_required
def instantiate_creator():
	return "nope"

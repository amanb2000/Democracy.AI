from di import app

@app.route("/")
def instantiate_home():
    return render_template("home.html")

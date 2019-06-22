from di import app

@app.route("/")
def instantiate_home():
    return render_template("schema1.html")

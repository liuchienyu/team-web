from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/news")
def news():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# antikythera?celestial_body=sun

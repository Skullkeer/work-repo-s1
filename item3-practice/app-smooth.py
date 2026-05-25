from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index_smooth.html")

@app.route("/smoothies")
def smoothies():
    return render_template("smoothies.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

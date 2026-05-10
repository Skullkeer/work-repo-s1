from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/name")
def hello_name():
    return "Hiiii Jadeyyyy"

@app.route("/test")
def serve_html():
    return render_template("hello.html")

@app.route("/ping")
def ping():
    return jsonify({"ok": True})

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)

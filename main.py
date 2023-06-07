from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/personal", methods=["GET"])
def personal():
    return "personal"

@app.route("/experience", methods=["GET"])
def experience():
    return "experience"

@app.route("/education", methods=["GET"])
def education():
    return "education"

if __name__ == "__main__":
    app.run()
from flask import Flask, request, jsonify
import parser

app = Flask(__name__)

@app.route("/personal", methods=["GET"])
def personal():
    data = parser.get_by_section("personal")
    return data

@app.route("/experience", methods=["GET"])
def experience():
    data = parser.get_by_section("experience")
    return data

@app.route("/education", methods=["GET"])
def education():
    data = parser.get_by_section("education")
    return data

if __name__ == "__main__":
    app.run()
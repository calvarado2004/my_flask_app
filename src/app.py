#!/usr/bin/env python3
import os

from flask import Flask, request, render_template

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')

app = Flask(__name__, template_folder=TEMPLATES_DIR)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return render_template("response.html", input_text=input_text)


if __name__ == '__main__':
    app.run(debug=True)

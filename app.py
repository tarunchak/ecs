from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def main_page ():
    return render_template('main.html')

@app.route('/<name>')
def member (name):
    return render_template("name.html", name=name)

    
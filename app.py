from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def main_page ():
    return render_template('main.html')

# @app.route('name/<name>')
# def member_page(name):
#     if name == "emeka":
#         return render_template('name/emeka.html', name=name)
#     if name == "kevin":
#         return render_template('name/kevin', name=name)
#     if name == "callum":
#         render_template('name/callum', name=name)
#     if name == "will":
#         return render_template('name/will', name=name)
    
# Further config access https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

from flask import Flask, render_template, jsonify, make_response

app = Flask(__name__,static_url_path='',static_folder='static', template_folder='templates')


@app.route("/", methods=['GET'])
def index_get():
    return render_template("index.html")

@app.route("/hello", methods=['GET'])
def hello_get():
    return make_response(jsonify({"hello": "world"}))
# start a flask app that opens index.html when run on a localhost
from flask import *
from datetime import datetime, timedelta
from random import randint

import requests
app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get(npoint_url)
    data = response.json()
    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')
    return render_template("index.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url, posts=data, datetime=datetime, randint=randint)


@app.route('/about')
def about():
    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')
    return render_template("about.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url)


@app.route('/contact')
def contact():
    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')
    return render_template("contact.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url)


@app.route('/post')
def post():
    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')
    return render_template("post.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url)

npoint_url = "https://api.npoint.io/674f5423f73deab1e9a7"



if __name__ == "__main__":
    app.run(debug=True)

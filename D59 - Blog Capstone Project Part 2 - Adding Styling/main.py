from flask import Flask, render_template, url_for
from datetime import datetime, timedelta
from random import randint
import requests

app = Flask(__name__)

npoint_url = "https://api.npoint.io/674f5423f73deab1e9a7"


@app.route('/')
def index():
    response = requests.get(npoint_url)
    data = response.json()

    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')

    return render_template("index.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url, posts=data,
                           datetime=datetime, randint=randint)


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


@app.route('/post/<int:post_id>')
def post(post_id):
    response = requests.get(npoint_url)
    data = response.json()

    requested_post = None

    for blog_post in data:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')

    return render_template("post.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url, post=selected_post,
                           datetime=datetime, randint=randint)



if __name__ == "__main__":
    app.run(debug=True)

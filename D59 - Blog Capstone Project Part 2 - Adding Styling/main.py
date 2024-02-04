# start a flask app that opens index.html when run on a localhost
from flask import *
app = Flask(__name__)


@app.route('/')
def index():
    css_url = url_for('static', filename='/css/styles.css')
    js_url = url_for('static', filename='/js/scripts.js')
    favicon_url = url_for('static', filename='/assets/favicon.ico')
    return render_template("index.html", css_url=css_url, js_url=js_url, favicon_url=favicon_url)


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


if __name__ == "__main__":
    app.run(debug=True)

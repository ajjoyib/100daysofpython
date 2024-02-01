# main.py
from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

def fetch_posts():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post_objects = [Post(post['id'], post['title'], post['subtitle'], post['body']) for post in posts]
    return post_objects

@app.route('/')
def get_all_posts():
    all_posts = fetch_posts()
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((post for post in fetch_posts() if post.id == index), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
OWN_EMAIL = "hamidullo287@gmail.com"
OWN_PASSWORD = "20@lfraganuS04"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    is_msg_sent = False
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        is_msg_sent = True
        return render_template("contact.html", is_msg_sent=is_msg_sent)
    return render_template("contact.html", is_msg_sent=is_msg_sent)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

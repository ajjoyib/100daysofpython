from flask import Flask

app = Flask(__name__)


@app.route("/")
def hellow_world():
    return ("<h1 style='text-align: center'>Hello World!</h1>"
            "<p>This is my first flask app.</p>"
            '<iframe src="https://giphy.com/embed/KPgOYtIRnFOOk" width="480" height="320" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/afvpets-afv-gorilla-KPgOYtIRnFOOk">via GIPHY</a></p>')


# def make_bold(func):
#     def wrapper_function():
#         return f'<b>{func()}</b>'
#     return wrapper_function
#
# def make_emphasis(func):
#     def wrapper_function():
#         return f'<em>{func()}</em>'
#     return wrapper_function
#
# def make_underline(func):
#     def wrapper_function():
#         return f'<u>{func()}</u>'
#     return wrapper_function

def make_format(tag):
    def decorator(func):
        def wrapper_function():
            return f'<{tag}>{func()}</{tag}>'
        return wrapper_function()
    return decorator()



@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underline
@make_format('b')
@make_format('em')
@make_format('u')
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greetings(name, number):
    return f"Hello {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)

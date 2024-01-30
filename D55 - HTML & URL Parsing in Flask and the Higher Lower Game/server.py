from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', message='Guess a number between 0 and 9')


@app.route("/<guessed_number>")
def result(guessed_number):
    try:
        guessed_number = int(guessed_number)
        if not 0 <= guessed_number <= 9:
            raise ValueError("Number out of range")

        random_number = random.randint(0, 9)
        print(f"Random Number: {random_number}")

        if guessed_number == random_number:
            return render_template('result.html', result='You found me!', color='green')
        elif guessed_number < random_number:
            return render_template('result.html', result='Too low, try again!', color='red')
        elif guessed_number > random_number:
            return render_template('result.html', result='Too high, try again!', color='red')

    except Exception:
        return render_template('result.html', result='Invalid input! Please enter a number between 0 and 9.',
                               color='red')


if __name__ == "__main__":
    app.run(debug=True)

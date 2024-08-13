from flask import Flask
import random

choice = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>"Guess a number between 0 and 9"</h1>'

@app.route("/<int:number>")
def guess(number):
    if number == choice:
        return "<h1 style='color: greeen'>you found me!</h1>" \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < choice:
        return "<h1 style='color: purple'>Too low, try again!</h1>" \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return "<h1 style='color: Red'>Too high, try again!</h1>" \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)

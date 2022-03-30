"""Greeting Flask app."""

from random import choice

from flask import Flask, request, render_template, url_for

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return render_template('index.html', title='Home Page')


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    global AWESOMENESS
    return render_template('hello.html', title='Hi there!', greetings=AWESOMENESS)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("greeting_list")

    return render_template('greeting.html', title='A Compliment', player=player, compliment=compliment)
  
  
@app.route('/dis')
def dis_person():
  """Insult a person"""
  insults = ['an idiot', 'brain-dead', 'slow', 'a moron', 'a vegetable']
  insult = choice(insults)
  return render_template('dis.html', title='Dis Master', insult=insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(port=5005, debug=True, host="0.0.0.0")

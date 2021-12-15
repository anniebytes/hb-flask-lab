"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
DISSES = [
    'smelly', 'mean', 'not nice']

# DISSES = [
#     'smelly']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <br>
    <a href= "/hello">take me to hello</a>
    </br>
    </html>"""

    
@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    options_html = ""
    for compliment in AWESOMENESS:
      options_html += f'<option value="{compliment}">{compliment}</option>'

    diss_html = ""
    for diss in DISSES:
      #diss_html += f'<option value="{diss}">{diss}</option>'
      diss_html += f"""
      <div>
        <input type="checkbox" id={diss} name="diss" value={diss}>
        <label for={diss}">{diss}</label>
      </div>

      """

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          Compliment someone <br>
          Name: <input type="text" name="person">
          <select name="compliment">
            {options_html}
          </select>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss" method="GET">
          Diss someone <br>
          Name: <input type="text" name="person">
          <fieldset>
          <legend>Choose a diss:</legend>
          {diss_html}
          </fieldset>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet', methods=["POST"])
def greet_person():
    """Get user by name."""
    player = request.form.get("person")

    compliment = request.form.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss', methods=["GET"])    
def diss():
    """Get user by name."""
    player = request.args.get("person")
    diss = request.args.get("diss")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}! boooo
      </body>
    </html>
    """ 
    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

This is not a tutorial, neither a real project, I'm just following the classes by Corey Schafer on YouTube:
https://www.youtube.com/user/schafer5/

TODO format this page

1. ###### Getting Started

To run the app on the terminal, first set an environment variable:
   `set FLASK_APP=flaskblog.py`
   
To actual run the app:
    `flask run`

To run in debug mode, first set:
    `set FLASK_DEBUG=1`

To configure different routs, use:
`@app.route('/home')`, followed by the function: `def home():`


2. ###### Templates

Are html files with the pages design.

In python, `from flask import render_template`

To add code to the html file, use:
`{% for x in y %}` and end with `{% endfor %}`

To print something in the html file, use:
`<h1> {{ post.title }} </h1>`

In a layout html file, is possible to create a block, with: `{% block content %} {% endblock %}`
where other html files can inherit and add code.

To extend from a layout file, use: `{% extends "layout.html" %}`,
to overwrite the codeblock, simply call `{% block content %} {% endblock %}` and write between the `}{`.
The endblock can also have the name of the block to indicate `{% endblock content %}`

To link file to the html file, use `from flask import url_for`

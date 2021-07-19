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

3. ###### Forms and User Input

For security, is important to set a random key on the main file, with:
`app.config['SECRET_KEY'] = '9cdfdeda8dcb694055c2af3ea51176ce'`

to generate a random key, on the python console:
`import secrets` and `secrets.token_hex(16)`, where 16 is the number of bytes

`{{ form.hidden_tag() }}` on the html of the register and login for security reasons

`from flask_wtf import FlaskForm` to work with forms.

`from wtforms import StringField` to get the fields.

`from wtforms.validators import DataRequired` are used to control data input settings

To allow the page to POST or GET, change in the main file:
`@app.route('/register', methods=['GET', 'POST'])`

To check for a submit action use: `if form.validate_on_submit():`

To display a message, use: `flash(f'Account created for {form.username.data}!', category='success')`

To redirect: use `return redirect(url_for('home'))`

4. ###### Database with Flask-SQLAlchemy

`from flask_sqlalchemy import SQLAlchemy` to import SQLAlchemy

`app.config['SQLALCHEMY_DATABASE_URI'] = 'db.create_all()` config teh app with the database

`db = SQLAlchemy(app)` to bind an instance of the app

The Models are classes that extend `db.Model`

each variable is a `db.Column`, with specific attributes

`primary_key` Used on the id Column to set a id

`unique=True` Can not repeat values

`nullable=False` Can not be empty

`default=` specify a default value

`posts = db.relationship('Post', backref='author', lazy=True)`
To connect the models

`backref='author'` A 'Column' on Post to reference the User

On the python console:

`db.create_all()` creates the file on `sqlite:///site.db`

`user_1 = User(username='DaT', email='a@b.com', password='asdf')`
Creates a new user.

`db.session.add(user_1)` to add the user to the database

`db.session.commit()` to commit the database to the file

`User.query.` to get the elements

Options of query:

`.all()` all

`.first()` first

`.filter_by(username='DaT').all()` to filter by a specific
parameter

The query can be saved on a variable

`.get(id)` get from the id

The user can be accessed from the post by `post.author`

To clear the database, use: `db.drop_all()`, this will need to be 
reconstructed by `db.create_all()`

5. ###### Package Structure

To create a package, need a folder with the same name of the project
and a file: `__init__.py`

Move every file and directory, except the main file (`flaskblog.py`) to the package

new files to models and routs, inside the package

rename `flaskblog.py` to `run.py`





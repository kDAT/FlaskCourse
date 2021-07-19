
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Configs
app = Flask(__name__)
app.config['SECRET_KEY'] = '9cdfdeda8dcb694055c2af3ea51176ce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Needs to be down here, because routs import app
from flaskblog import routes

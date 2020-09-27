from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, template_folder='../templates')
bootstrap = Bootstrap(app)
app.config.from_object(Config)

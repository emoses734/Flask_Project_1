# Here we are importing flask
from flask import Flask

# Define "app" as flask object.
app = Flask(__name__)

from app import routes

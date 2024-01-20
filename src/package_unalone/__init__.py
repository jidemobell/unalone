from flask import Flask

app = Flask(__name__)

from src.package_unalone import routes, example

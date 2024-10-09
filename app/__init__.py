from flask import Flask
import os

template_dir = os.path.abspath('app/templates')
app = Flask(__name__, template_folder=template_dir)

from app import routes
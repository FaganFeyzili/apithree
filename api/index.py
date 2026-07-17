from flask import flask 
from flask_cors import CORS 

app = Flask(__name__)

CORS(app, resources={r"/api/news": {
    "origins": [],
    "methods": ["GET"]
}})

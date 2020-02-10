from flask import *
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return "initial page"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

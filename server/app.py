from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# routes
@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
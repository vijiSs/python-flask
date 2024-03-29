# app.py
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application if the script is executed
if __name__ == '__main__':
    app.run(debug=True)


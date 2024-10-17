from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Home Energy Management System"

if __name__ == "__main__":
    app.run(debug=True)

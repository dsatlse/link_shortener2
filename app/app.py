import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

base_url = "https://dsatlse.github.io/linky"

@app.route('/<short_url>')
def redirect_to_firebase(short_url=None):
    return redirect(f"{base_url}/{short_url}")

@app.route('/')
def hello():
    return "Try typing 'http://127.0.0.1:5000/random_word'"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

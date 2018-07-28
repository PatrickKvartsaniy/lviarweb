import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    host, port = '0.0.0.0', int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port,debug=True)
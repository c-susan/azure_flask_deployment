from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
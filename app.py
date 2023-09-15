from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def aboutpage(): 
    return render_template('about.html')


df = pd.read_csv('https://raw.githubusercontent.com/c-susan/azure_flask_deployment/main/data/OPIOID_TREATMENT_PROGRAM_PROVIDERS_08282023.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
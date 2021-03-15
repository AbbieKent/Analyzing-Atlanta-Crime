from flask import Flask, render_template
from flask import request, url_for, render_template, redirect
import pandas as pd
import numpy as np
import pdb, os
from os import environ
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import LabelEncoder

from platform import python_version
print(python_version())

# Create an instance of our Flask app.
app = Flask(__name__)
# Set route
@app.route('/')
def index():
    print('STARTING! '*20)
    mapbox_access_token = "pk.eyJ1IjoiZGF2aWRjb3kiLCJhIjoiY2tqcHU1YzBzOHY4ZjJxcWpkNGI5b2h2MSJ9.CsPttIW0Q41kP2uOBN6n8g"
    # pdb.set_trace()
    print(os.getcwd())
    # df = pd.read_csv('./static/data/data.csv')
    df = pd.read_csv('./static/data/data.csv')
    #df = df.head(5)
    return render_template('index.html', tables = [df.to_html(classes='female')],
        titles=['IDKLOL'],
        mapbox_access_token=mapbox_access_token)
@app.route('/neighborhood')
def neighborhood():
    return render_template('neighborhood.html')
@app.route('/typesofcrimes')
def crime():
    return render_template('crime.html')
@app.route('/timeofyear')
def year():
    return render_template('Timeofyear.html')
@app.route('/contactinfo')
def contact():
    return render_template('contactinfo.html')
@app.route('/index')
def homepage():
    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)

from sklearn.linear_model import LogisticRegression
import numpy as np
from flask import Flask, request, render_template
from flask.helpers import url_for
import os
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')


@app.route('/eligibility.html/', methods=['GET'])
def eligibility():
    return render_template('eligibility.html')

@app.route('/about.html/', methods=['GET'])

def about():
    return render_template('about.html')




if __name__ == "__main__":
    app.run(debug=True)

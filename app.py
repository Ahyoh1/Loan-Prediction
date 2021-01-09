from sklearn.linear_model import LogisticRegression
import numpy as np
from flask import Flask, request, render_template
from flask.helpers import url_for
import os
from werkzeug.utils import redirect
import joblib

model_file = joblib.load('model_loan.sav')


app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')


@app.route('/eligibility.html/', methods=['GET'])
def eligibility():
    return render_template('eligibility.html')

@app.route('/check', methods=['POST'])


def check():
    if request.method == 'POST':
        genders = request.form['genders']
        if genders == 'male':
            genders = np.array([0, 1])
        elif genders == 'selected':
            return render_template('eligibility.html')
        else:
            genders = np.array([1, 0])
        marital = request.form['marital']
        if marital == 'married':
            marital = np.array([0, 1])
        else:
            marital = np.array([1, 0])
        depends = request.form['dependent']
        if depends == 'zero':
            depends = np.array([1, 0, 0, 0])
        elif depends == 'one':
            depends = np.array([0, 1, 0, 0])
        elif depends == 'two':
            depends = np.array([0, 0, 1, 0])
        else:
            depends = np.array([0, 0, 0, 1])
        edu = request.form['education']
        if edu == 'graduate':
            edu = np.array([1, 0])
        else:
            edu = np.array([0, 1])
        employ = request.form['self-employ']
        if employ == 'yes':
            employ = np.array([0, 1])
        else:
            employ = np.array([1, 0])
        income = request.form['income']
        income = np.array([int(income)])
        co_income = request.form['co-income']
        co_income = np.array([int(co_income)])
        loan = request.form['loan-amount']
        loan = np.array([int(loan)])
        days = request.form['term']
        days = np.array([int(days)])
        history = request.form['credit-history']
        if history == 'zero':
            history = np.array([0])
        else:
            history = np.array([1])
        area = request.form['settlement']
        if area == 'urban':
            area = np.array([0, 0, 1])
        elif area == 'rural':
            area = np.array([1, 0, 0])
        else:
            area = np.array([0, 1, 0])

        output = model_file.predict(np.array([np.concatenate((genders, marital, depends, edu, employ, area, 
                          income, co_income, loan, days, history), axis=0)]))   
        if output == 1:
            return render_template('result.html', prediction='eligible')
        else:
            return render_template('result.html', prediction='not eligible')
    
    else:
        return render_template('index.html')




@app.route('/about.html/', methods=['GET'])

def about():
    return render_template('about.html')




if __name__ == "__main__":
    app.run(debug=True)

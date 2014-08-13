import os
from numeralConverter import convert
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

@app.route('/numberform', methods=['POST'])
def numberform():
    num = int(request.form['number'])
    session['numeral'] = convert(num)
    return redirect('/goodbye')

if __name__ == '__main__':
    app.secret_key = 'aasdifjapoaopsifpowj234234j0f9w8f209r8'
    app.run(debug = True, use_reloader=True)
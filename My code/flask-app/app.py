from email import message
from flask import Flask, render_template, request, redirect, url_for

"""
It creates an instance of the Flask Class.
Which will be the Web Server Gateway Interface (WSGI) application.
"""


### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return 'Welcome to the Flask App! Ya Neygga!!!'

@app.route("/index", methods = ['GET'])
def welcome_to_index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/submit1", methods = ['GET', 'POST'])
def submit1():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('form.html')

## Variable rule
@app.route("/user/<int:score>")
def user(score):
    return f'The score of this user is {score}'

@app.route("/success/<int:score>")
def success(score):
    res = ''
    if score < 50:
        res = "fail"
    else:
        res = 'pass'

    exp = {'score' : score, 'result' : res}

    return render_template('result.html', message = exp)

@app.route("/success_res/<int:score>")
def success_res(score):
    res = ''
    if score < 50:
        res = "fail"
    else:
        res = 'pass'

    exp = {'score' : score, 'result' : res}

    return render_template('result1.html', message = exp)

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    avg_score = 0
    if request.method == 'POST':
        science_score = float(request.form["science"])
        math_score = float(request.form["maths"])
        c_score = float(request.form["c"])
        ds_score = float(request.form["datascience"])
    else:
        return render_template('getresult.html')

    avg_score = (science_score + math_score + c_score + ds_score)/ 4

    return redirect(url_for('success_res', score = avg_score))




"""
Jinja 2 template helps us to display the message in HTML with {{ message }}
conditional statements can be types using {% if score < 50 %} {% else %} {% endif %} or {% ..... %}
loops can be used using {% for item in items %} {% endfor %} or {% ..... %}
Comments can be added using {# comment #}
""" 


if __name__ == "__main__":
    app.run(debug=True)
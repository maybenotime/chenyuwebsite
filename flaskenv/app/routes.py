from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/example')
def show():
    user = {'username': '某不知名小学生'}
    return render_template('example.html', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='登 录', form=form)

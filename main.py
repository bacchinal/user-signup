from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')

def index():
    return render_template('user_form.html')

@app.route('/', methods=['POST'])
def verify_form():
    name = request.form['username']
    password = request.form['password']
    verify = request.form['verify'] 
    email = request.form['email']
    name_error = ''
    password_error = ''
    email_error = ''

    if len(name) < 3 or len(name) > 19:
        name_error = 'Sorry! That username is invalid. Please try again.'
        name = ''
    if len(password) < 3 or len(password) > 19:
        password_error = "Uh oh! That won't work. Try again."
    if name == '':
        name_error = 'Hello, friend. Please enter a username.'
        name = ''
    if password == '':
        password_error = 'Passwords are important. Please enter yours now.'
        password = ''
        verify = ''

    if verify == '':
        verify_error = "Can't skip this step. Passwords must match. Please retry."
        password = ''
        verify = ''

    if not password == verify:
        password_error = "OOPSY! Passwords must match. Please retry."
        password = ''
        verify = ''
    if not email == '':
        if " " in email:
            email_error = "That won't work for me. Please try again."
            email = ''
        elif not email.count('@') == 1:
            email_error = "That must be a typo. Please try again."
            email = ''
        elif not email.count('.') == 1:
            email_error = "Hmm. That doesn't look right. Please try again."
            email = ''
        elif len(email) < 3 or len(email) > 19:
            email_error = "Well, that just won't do. Please try again."

    if not name_error and not password_error and not email_error:
       
        return render_template('welcome-user.html', user=name)
    else:
        
        return render_template('user_form.html', name_error=name_error, password_error=password_error, name=name, email=email, email_error=email_error) 



app.run()
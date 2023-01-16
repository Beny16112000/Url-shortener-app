from flask import Flask, render_template, Blueprint, redirect, request
from flask_login import current_user, login_required
from .models import User, UrlShortener
from .authentication.user import UserClass
from .UrlShortener.link import Link, LinkData
import requests


main = Blueprint('main', __name__) 


@main.route('/')
def index():
    """
    Handle landing client
    """
    if current_user.is_authenticated:
        return redirect(f'/panel/{current_user.email}/main')
    else:
        return redirect('/auth/login')



@main.route('/auth/register', methods=['GET', 'POST'])
def register():
    """
    Register page
    """
    message = ''
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        
        if pass1 != pass2:
            message = 'Password dont match !'
            return render_template('register.html', message=message)

        user = User.query.filter_by(email=email).first()
        if user:
            message = 'Email alaredy exist'
            return render_template('register.html', message=message)
        else:
            save = UserClass().register(fname, lname, email, pass1)
            if save is not None:
                return redirect('/auth/login')
    return render_template('register.html', message=message)



@main.route('/auth/login', methods=['GET', 'POST'])
def login():
    """
    Login page
    """
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        sing_in = UserClass().sing_in(email, password)

        if sing_in is not None:
            return redirect('/')
        else:
            message = 'Email or password dont match our data !'
            return render_template('login.html', message=message)

    return render_template('login.html', message=message)



@main.route('/auth/logout')
@login_required
def logout():
    """
    Logout endpoint
    """
    UserClass().sing_out()
    return redirect('/')



@main.route('/panel/<email>', methods=['GET', 'POST'])
@login_required
def panel(email):
    """
    Create links Panel
    """
    message = ''
    if request.method == 'POST':
        url = request.form.get('url')
        shorter = request.form.get('shorter')
        save = Link(current_user.id, url, 'http://127.0.0.1:5000/shorti/'+shorter, 0).create()
        if save is not True:
            return render_template('link.html', message=save)
        else:
            return redirect(f'/panel/{current_user.email}/main')
    return render_template('link.html')



@main.route('/panel/<email>/main')
@login_required
def panelMain(email):
    """
    Main Panel - display
    """
    urls = LinkData().getall(current_user.id).all()
    return render_template('panel.html', urls=urls)



@main.route('/shorti/<url>')
def redirector(url):
    """
    Main redirector
    """
    if current_user.is_authenticated:
        to = LinkData().redirector(url, False)
        return redirect(f'{to.url}')
    else:
        to = LinkData().redirector(url, True)
        return redirect(f'{to.url}')



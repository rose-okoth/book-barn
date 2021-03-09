from flask import render_template, redirect, url_for,abort,request,flash
from . import main
from flask_login import login_required,current_user
from ..models import User
from .. import db,photos
from ..email import mail_message

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    return render_template('index.html', title=title)
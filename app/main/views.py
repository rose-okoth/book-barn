
from flask import render_template, redirect, url_for,abort,request,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Subscriber
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

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Book Barn!","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Successfully subscribed!')
    return redirect(url_for('main.index'))


    title = 'Books'
    return render_template('index.html',title = title)

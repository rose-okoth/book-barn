from flask import render_template, redirect, url_for,abort,request,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Subscriber
from .. import db,photos
from ..email import mail_message
from .forms import UpdateProfile
import datetime
from ..request import get_books

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
  
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/library/')
def library():
    '''
    View library page function that returns library page and its
    data
    '''
    my_books = get_books()
    
    return render_template('library.html',books = my_books)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # books_count = Book.count_books(uname)
    # user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

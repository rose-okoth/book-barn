from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,CommentForm
from ..models import User,Review,Comment
from ..request import get_quote
from flask_login import login_required,current_user
from .. import db
import markdown2

# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home -Review page'
    content = "WELCOME TO BOOK-BARN WEBSITE"
    quote = get_quote()

    return render_template('index.html', title = title,content = content,quote = quote)


@main.route('/review/new_review', methods = ['GET','POST'])
def new_review():
    quote = get_quote()

    form = ReviewForm()

    if form.validate_on_submit():
        review= form.description.data
        title=form.review_title.data

        # Updated review instance
        new_review = Review(review_title=title,description= review,user_id=current_user.id)

        title='New review'

        new_review.save_review()

        return redirect(url_for('main.new_review'))

    return render_template('review.html',form= form, quote=quote)

@main.route('/review/all', methods=['GET', 'POST'])
def all():
    reviews = Review.query.all()
    quote = get_quote()
    return render_template('reviews.html', reviews=reviews, quote=quote)
@main.route('/comments/<id>')
def comment(id):
    '''
    function to return the comments
    '''
    quote = get_quote()
    comm =Comment.get_comments(id)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title,quote=quote)

@main.route('/new_comment/<int:review_id>', methods = ['GET','POST'])
def new_comment(review_id):
    quote = get_quote()
    reviews = Review.query.filter_by(id = review_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment,user_id=current_user.id, review_id=review_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New comment'
    return render_template('new_comment.html',title=title,comment_form = form,review_id=review_id,quote=quote)

@main.route('/view/<int:id>', methods=['GET', 'POST'])
def view(id):
    # review = Review.query.get_or_404(id)
    review_comments = Comment.query.filter_by(review_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(review_id=id, comment=comment_form.comment.data, username=current_user)
        new_comment.save_comment()

    return render_template('view.html', review=review, review_comments=review_comments, comment_form=comment_form)




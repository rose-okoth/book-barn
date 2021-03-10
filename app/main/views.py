from flask import render_template
from . import main

# Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     title = 'Home'
#     return render_template('index.html', title=title)

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Book-barn website'
    content = "WELCOME TO BOOK-BARN WEBSITE"
    quote = get_quote()

    return render_template('index.html', title = title,content = content,quote = quote)

@main.route('/user/<uname>')
def profile(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, quote=quote)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form, quote=quote)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    quote = get_quote()
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/writer/<uname>/update/pic',methods= ['POST'])
@login_required
def update_writer_pic(uname):
    quote = get_quote()
    writer = Writer.query.filter_by(writer_name = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        Writer.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/opinion/new_opinion', methods = ['GET','POST'])
@login_required
def new_opinion():
    quote = get_quote()

    form = OpinionForm()

    if form.validate_on_submit():
        opinion= form.description.data
        title=form.opinion_title.data

        # Updated opinion instance
        new_opinion = Opinion(opinion_title=title,description= opinion,user_id=current_user.id)

        title='New opinion'

        new_opinion.save_opinion()

        return redirect(url_for('main.new_opinion'))

    return render_template('opinion.html',form= form, quote=quote)

@main.route('/opinion/all', methods=['GET', 'POST'])
@login_required
def all():
    opinions = Opinion.query.all()
    quote = get_quote()
    return render_template('opinions.html', opinions=opinions, quote=quote)
@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    quote = get_quote()
    comm =Comment.get_comments(id)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title,quote=quote)

@main.route('/new_comment/<int:opinion_id>', methods = ['GET','POST'])
@login_required
def new_comment(opinion_id):
    quote = get_quote()
    opinions = Opinion.query.filter_by(id = opinion_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment,user_id=current_user.id, opinion_id=opinion_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New comment'
    return render_template('new_comment.html',title=title,comment_form = form,opinion_id=opinion_id,quote=quote)

@main.route('/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view(id):
    opinion = Opinion.query.get_or_404(id)
    opinion_comments = Comment.query.filter_by(opinion_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(opinion_id=id, comment=comment_form.comment.data, username=current_user)
        new_comment.save_comment()

    return render_template('view.html', opinion=opinion, opinion_comments=opinion_comments, comment_form=comment_form)

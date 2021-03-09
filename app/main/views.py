from flask import render_template
from . import main
from ..models import Subscriber

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    return render_template('index.html', title=title)

# @main.route('/blog/new', methods = ['GET','POST'])
# @login_required
# def new_blog():
#     subscribers = Subscriber.query.all()
#     blog_form = BlogForm()
#     if blog_form.validate_on_submit():
#         title = blog_form.title.data
#         blog = blog_form.text.data
#         category = blog_form.category.data
#         user_id =  current_user._get_current_object().id

#         # Updated blog instance
#         new_blog = Blog(blog_title=title,blog_content=blog,category=category,user=current_user)

#         # Save blog method
#         new_blog.save_blog()
#         for subscriber in subscribers:
#             mail_message("New Blog Post","email/new_blog",subscriber.email,new_blog=new_blog)
#         return redirect(url_for('.index'))
#         flash('You Posted a new blog')

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Zen Blog","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Successfully subscribed')
    return redirect(url_for('main.index'))


    title = 'New blog'
    return render_template('create_post.html',title = title,blog_form=blog_form )

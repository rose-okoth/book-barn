from . import db
from . import login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from datetime import datetime

# class Book:
#     '''
#     Book class to define Book Objects
    # '''


  
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer())
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    review = db.relationship('Review', backref='username', lazy='dynamic')
    comments = db.relationship('Comment', backref='username', lazy=True)
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    review_title = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Post.query.filter_by(id=id).all()
        return reviews

    @classmethod
    def get_all_reviews(cls):
        reviews = Reviews.query.order_by('-id').all()
        return reviews

    def __repr__(self):
        return f'Posts {self.reviews_title}'
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, review_id):
        comments = Comment.query.filter_by(review_id=review_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
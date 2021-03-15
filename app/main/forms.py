from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
    
class ReviewForm(FlaskForm):
    review_title = StringField('Review Title')
    description = TextAreaField('Review')
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post a comment')
    
    

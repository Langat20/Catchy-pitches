from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
     comment = TextAreaField('Comment',validators = [DataRequired()])
     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
     title = StringField('Title',validators = [DataRequired()])
     category = SelectField('Category', choices= [('Email','Email'),('Business Idea','Business Idea'),('Social Media','Social Media')],validators=[DataRequired()])
     pitch_text = TextAreaField('Write your pitch',validators = [DataRequired()])
     submit = SubmitField('Submit')
from flask import render_template,redirect,url_for,abort,request
from idna import valid_string_length
from . import main
from .forms import CommentForm,UpdateProfile,PitchForm
from ..models import User,Comments,Pitches,Likes,Dislikes
from flask_login import login_required, current_user
from .. import db
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitches.query.all()
    email = Pitches.query.filter_by(category = 'Email').all()
    business = Pitches.query.filter_by(category = 'Business Idea').all()
    social = Pitches.query.filter_by(category = 'Social Media').all()
    title = 'Home - Welcome to Pitches site'

    
    return render_template('index.html',pitches = pitches, email = email,business = business,social = social,title = title)

@main.route('/pitch/',methods = ['GET','POST'])
@login_required
def pitch_form():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch_text = pitch_form.pitch_text.data
        category = pitch_form.category.data
        
        new_pitches = Pitches(pitch_text=pitch_text,category=category,user_id=current_user._get_current_object().id,title = title)
        new_pitches.save_p()
        return redirect(url_for('main.index', ))

    return render_template('new_pitch.html', pitch_form=pitch_form )


@main.route('/comment/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def comment(pitch_id):
    comment_form = CommentForm()
    pitches = Pitches.query.get(pitch_id)
    comments = Comments.get_comment(pitch_id)
    user = User.query.filter_by(id=id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        
        # Updated comment instance
        new_comment = Comments(pitch_id=pitch_id,comment=comment,user_id=current_user.get_id())
        # save comment method
        new_comment.save()
        return redirect(url_for('main.comment',pitch_id = pitch_id ))

    return render_template('comment.html',comment_form=comment_form,pitches=pitches,comments=comments,user=user)
    

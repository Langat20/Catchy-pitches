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


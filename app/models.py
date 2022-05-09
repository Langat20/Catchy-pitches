from flask_login import UserMixin
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    comments = db.relationship('Comments',backref = 'comments',lazy = "dynamic")
    pitches = db.relationship('Pitches',backref = 'author',lazy = "dynamic")
    likes = db.relationship('Likes', backref = 'user', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'user', lazy = 'dynamic')
    @property
    def password(self):
        raise AttributeError('You cannnot access this attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'
    
class Comments(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save(self,):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,pitch_id):
        comments = Comments.query.filter_by(pitch_id=pitch_id).all()
        return comments
    
    def __repr__(self):
        return f'Comment {self.pitch_comment}'
class Pitches(db.Model):
    
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    pitch_text = db.Column(db.String(400))
    posted = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('Likes', backref = 'pitch', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'pitch', lazy = 'dynamic')
    comments = db.relationship('Comments', backref = 'pitch', lazy='dynamic')
    def save_p(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_category(cls, category):
        pitches = Pitches.query.filter_by(category=category).all()
        return pitches
  
    
class Likes(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        likes= Likes.query.filter_by(pitch_id =id).all()
        return likes
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Dislikes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls,id):
        dislikes = Dislikes.query.filter_by(pitch_id =id).all()
        return dislikes
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
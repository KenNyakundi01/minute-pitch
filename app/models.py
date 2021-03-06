from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot access this property')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self):
        db.session.add(self)
        db.session.commit()

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), index=True)
    pitches=db.relationship('Pitch', backref= 'category', lazy='dynamic')
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_cats(cls):
        categorys = Category.query.all()
        return categorys
    


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    content = db.Column(db.String(255))
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(category_id=category)
        return pitches

    @classmethod
    def get_pitch_by_id(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    @classmethod
    def get_all_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id= id).all()
        return comments


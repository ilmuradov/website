from flask import Flask, session, redirect, url_for, request
from datetime import datetime
from app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(266), index=True, unique=True)
    password_hash = db.Column(db.String(266))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, username, **kwargs):
        return redirect (url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(app, index_view=MyAdminIndexView())


class Head(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(266))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Head {}>'.format(self.title)

admin.add_view(MyModelView(Head, db.session))


class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sec_title = db.Column(db.String(266))
    sec_body = db.Column(db.Text)
    sec_timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Body {}>'.format(self.sec_title)

admin.add_view(MyModelView(Body, db.session))


class Footer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    third_title = db.Column(db.String(266))
    third_body = db.Column(db.Text)
    third_timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Footer {}>'.format(self.third_title)

admin.add_view(MyModelView(Footer, db.session))

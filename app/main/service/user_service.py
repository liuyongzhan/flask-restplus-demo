import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return None, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '用户已存在，请直接登录。',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def update_user(public_id, data):
    user = User.query.filter_by(public_id=public_id).one()
    user.email = data.get('email')
    user.username = data.get('username')
    user.password = data.get('password')
    save_changes(user)


def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).one()
    save_del(user)


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def save_del(data):
    db.session.delete(data)
    db.session.commit()


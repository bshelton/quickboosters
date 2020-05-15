#add and delete users
from flask import request, jsonify
from quickboosters.api.users import auth
from quickboosters.api.users.forms import RegistrationForm
from quickboosters.api.users.models import User
from passlib.hash import sha256_crypt
from quickboosters import db
from quickboosters.api.users.forms import AccountDeactivation


@auth.route('/users/all', methods=['GET'])
def get_all_users():
    users_dict = {}
    users = User.query.filter_by().all()
    print(users)
    print(type(users))

    for user in users:
        users_dict[user.id] = {"username": user.username, "password": user.password, "email": user.email,"Role": user.role}
 
    return jsonify(users_dict)

@auth.route('/users/<user>', methods=['GET'])
def get_one_user(user):
    try:
        user_dict = {}
        user = User.query.filter_by(username=user).first()
        user_dict[user.id] = {"username": user.username, "password": user.password, "email": user.email,"Role": user.role}
        return jsonify(user_dict)
    except AttributeError as e:
        print(e)
    
    return user.username

@auth.route('/users/<int:id>', methods=['GET'])
def get_id(id):
    user_dict={}
    user = User.query.filter_by(id=id).first()
    user_dict[user.id] = {"username": user.username, "password": user.password,"email": user.email, "role": user.role}

    return jsonify(user_dict)
    

@auth.route('/users/role/<role>', methods=['GET'])
def get_admin(role):
    user_dict={}

    tom = User("tom", "tom@tom", "pass", role="none")
    print(type(tom))
    print(tom.password)

    users = User.query.filter_by(role=role).all()
    for user in users:
        user_dict[user.id] = {"username":user.username, "password": user.password, "email": user.email, "role": user.role}
        
    return jsonify(user_dict)


@auth.route('/users/<username>', methods=['POST'])
def mod_user(username):
    """
    remove privileges
    """
    user_dict={}
    user = User.query.filter_by(username=username).first()
    
    try:
        if user.role == 'Admin':
            user.role = 'None'
            db.session.commit()
            user_dict["message"] = user.username + ' changed from admin to none'
            return jsonify(user_dict)
    except Exception as e:
        print(e)
    

@auth.route('/users/makeadmin/<username>', methods=['POST'])
def make_admin(username):
    """
    add privileges
    """
    user_dict={}
    user = User.query.filter_by(username=username).first()

    try:
        if user.role != 'Admin':
            user.role = 'Admin'
            db.session.commit()
            user_dict['message'] = user.username + ' grats u r adman'
            return jsonify(user_dict)
    except Exception as e:
        print(e)


@auth.route('/users/delete/<username>', methods=['DELETE'])
def deleteuser(username):
    """
    Delete user
    """
    user = User.query.filter_by(username=username).first()

    try:
        db.session.delete(user)
        db.session.commit()
        return 'User ' + user.username + ' was deleted from the database'
    except Exception as e:
        print(e)
    
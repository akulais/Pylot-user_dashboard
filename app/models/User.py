from system.core.model import *
import re
from flask import flash
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def add_user(self, user):
    	EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not user['first_name']:
            errors.append('first name cannot be blank')
        elif len(user['first_name']) < 2:
            errors.append('Your first name is too short')

        if not user['last_name']:
            errors.append('last name cannot be blank')
        elif len(user['last_name']) < 2:
            errors.append('Your last name is too short')

        if not user['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Email format must be valid!')
        if not user['password']:
            errors.append('Password cannot be blank')
        elif len(user['password']) < 8:
            errors.append('Your password must be at least 8 characters long')
        elif user['password'] != user['cfm_pwd']:
            errors.append('Password and confirmation must match')

        if errors:
            return {'status': False, 'errors': errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(user['password'])
            # users = self.db.query_db("SELECT * FROM users")
            # try:
            # 	users
            # 	user_level = 1
            # except:
            # 	user_level = 9
            query = "INSERT INTO users (email, first_name, last_name, password, user_level, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
            values = [user['email'], user['first_name'], user['last_name'], hashed_pw, user_level]
            self.db.query_db(query, values)
            
            # get_user = "SELECT * FROM users ORDER BY id LIMIT 1"
            # user = self.db.query_db(get_user)
            return {'status' : True, 'user' : user[0]}
    	

    

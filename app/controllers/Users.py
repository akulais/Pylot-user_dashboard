"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import re
from flask import Flask, session, Markup, flash
import random
import requests
from time import strftime
import string
import pprint
string.letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.letters)

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        return self.load_view('user/index.html')

    def signin(self):
        return self.load_view('user/signin.html')

    def register(self):
        return self.load_view('user/register.html')

    def create_user(self):
        # print 'here'
        user = {
            "email" : request.form['email'],
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "password" : request.form['password'],
            "cfm_pwd" : request.form['cfm_pwd']
        }
        # print user
        user_status = self.models['User'].add_user(user)
        if (user_status['status'] == True):
            session['id'] = user_status['user']['id']
            session['first_name'] = user_status['user']['first_name']
            return redirect('/signin')
        else:
            for message in user_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    # def login(self):
    #     user_login = {
    #         "email" : request.form['email'],
    #         "password" : request.form['password']
    #     }

    #     login_status = self.models['User'].get_by_email(user_login)
    #     if (login_status['status'] == True):
    #         session['id'] = login_status['user']['id']
    #         session['first_name'] = login_status['user']['first_name']
    #         return redirect('/users/success_load')
    #     else:
    #         for message in user_status['errors']:
    #             flash(message, 'regis_errors')
    #         return redirect('/')

    


        
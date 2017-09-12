#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import auth
from flask import render_template,redirect,url_for,request,flash
from ..models import User
from .. import db
from flask_login import login_user


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        passwd = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if email == user.email and user.verify_password(passwd):
            print email
            print user.username
            print user.verify_password(passwd)
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('.login'))

@auth.route('/register',methods=['GET','POST'])

def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        passwd1 = request.form['password1']
        passwd2 = request.form['password2']
        if User.query.filter_by(username=username).first():
            flash(u'用户名已使用')
            return redirect(url_for('auth.login'))
        elif  User.query.filter_by(email=email).first():
            flash(u'邮箱已使用')
            return render_template('register.html')
        elif passwd1 != passwd2:
            flash(u'密码不一致')
            return render_template('register.html')
        else:
            user = User(email=email,
                        username=username,
                        password=passwd1)
            db.session.add(user)
            db.session.commit()
            flash(u'注册成功')
            return redirect(url_for('auth.login'))

    return render_template('register.html')
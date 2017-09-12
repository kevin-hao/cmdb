#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import main
from flask import render_template,request
from flask_login import login_required
from ..models import User

@main.route('/',methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

@main.route('/group_profile',methods=['GET','POST'])
def group_profile():
    return render_template('group_profile.html')

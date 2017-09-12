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
    return render_template('group_profile.html')from . import main
from flask import render_template,request,flash,redirect
from app.models import Department,Host,IDC,Business_group,Business
from sqlalchemy import and_
from flask import jsonify,Response
import json

import time


@main.route('/',methods=['GET','POST'])
def index():
    hosts = Host.query.all()
    host_length = len(hosts)


    return render_template('index.html',host=hosts,len=host_length,dep=Department,idc=IDC,buseniss=Business)

@main.route('/add_host',methods=['GET','POST'])
def Add_Host():
    dep = Department.query.all()
    dep_length = len(dep)
    idc = IDC.query.all()
    idc_length = len(dep)
    if request.method == "POST":
        hostname = request.form["hostname"]
        asset_num = request.form["asset_num"]
        inner_ip = request.form["inner_ip"]
        out_ip = request.form["out_ip"]
        control_ip = request.form["control_ip"]
        vip = request.form["vip"]
        department = request.form["depart"]
        b_idc = request.form["idc"]
        print hostname
        if hostname == '':
            print(u'主机名不能为空')


    return render_template('add_host.html',dep=dep,dep_len=dep_length,idc=idc,idc_len=idc_length)

@main.route('/viewhost/<int:id>',methods=['GET','POST'])
def View_Host(id):
    hosts = Host.query.get(id)
    return render_template('view_host.html',host=hosts,dep=Department,idc=IDC,buseniss=Business)

@main.route('/edithost/<int:id>',methods=['GET','POST'])
def Edit_Host(id):
    hosts = Host.query.get(id)
    return render_template('edit_host.html', host=hosts, dep=Department, idc=IDC, buseniss=Business)

@main.route('/distribute',methods=['GET','POST'])
def DisFile():
    return render_template('distribute_file.html')

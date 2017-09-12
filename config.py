#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class Config:
    # CSRF
    SECRET_KEY = 'hard to guess string'
    # Database
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Mail
    MAIL_SERVER = 'staff.easou.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'kade_hao@staff.easou.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'kade8888'
    CMBD_MAIL_SUBJECT_PREFIX = 'cmdb'
    CMDB_MAIL_SENDER = 'kade_hao<kade_hao@staff.easou.com>'
    CMDB_ADMIN = os.environ.get('BLOG_ADMIN') or '18189896229@163.com'
    CMDB_POSTS_PER_PAGE = 2

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kevin:123456@10.0.1.4/cmdb'

config = {
    'dev':DevConfig,
    'default':DevConfig
}
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
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '***********'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '******'
    CMBD_MAIL_SUBJECT_PREFIX = 'cmdb'
    CMDB_MAIL_SENDER = '***********'
    CMDB_ADMIN = os.environ.get('BLOG_ADMIN') or '********'
    CMDB_POSTS_PER_PAGE = 2

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@IP/database'

config = {
    'dev':DevConfig,
    'default':DevConfig
}

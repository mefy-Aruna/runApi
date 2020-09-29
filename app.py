# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:14:33 2020

@author: Aruna
"""

from flask import Flask

UPLOAD_FOLDER = 'C:/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
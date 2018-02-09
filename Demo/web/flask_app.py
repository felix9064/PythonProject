#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用Flask框架开发一个简单的web app
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/sign', methods=['GET'])
def sign_form():
    return '''<form action="/sign" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/sign', methods=['POST'])
def sign():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == "__main__":
    app.run()

from flask import request, render_template, current_app


@current_app.route('/')
def hello():
    return "hello"

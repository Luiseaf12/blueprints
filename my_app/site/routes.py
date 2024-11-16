from flask import Blueprint

site  = Blueprint('site',__name__)

@site.route('/')
def index():
    return '<h1> Bienvenido al site ! </h1>'
    
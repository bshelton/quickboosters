from flask import Blueprint

from quickboosters.config import Config

home = Blueprint('home',
                 __name__,
                 url_prefix='',
                 static_folder=Config.static_folder,
                 template_folder=Config.template_folder)

from quickboosters.frontend.home import controller
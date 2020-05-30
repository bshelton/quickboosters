from flask import Blueprint

chat = Blueprint('chat', __name__)

from quickboosters.api.chat import controller

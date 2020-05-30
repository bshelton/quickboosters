from flask import request
from quickboosters.api.chat import chat


@chat.route('/chat', methods=["POST"])
def chat_test():
    data = request.get_json() 
    print(data)
    return "Chat"
from flask import jsonify
from quickboosters.api.chat.models import ChatLog
from quickboosters.api.chat import chat

@chat.route('/chat', methods=['GET'])
def get_all_chat_logs():
    chatlogs_dict = {} 
    chat = getchat.query.filter_by().all()
for chat in getchat:
    chatlogs_dict[chat] {"ID": chat.id, "message": chat.message, "Userfrom": chat.userfrom, "Created_Date": chat.Created_Date, "Room": chat.room}
return jsonify(chatlogs_dict)
from flask import jsonify
from quickboosters.api.chat.models import ChatLog
from quickboosters.api.chat import chat

@chat.route('/chat/getlogs/all', methods=['GET'])
def get_all_chat_logs():
    chatlogs_dict = {} 
    logs = ChatLog.query.filter_by().all()
    for log in logs:
        chatlogs_dict[log] = {"ID": log.id,
        "message": log.message,
        "Userfrom": log.userfrom,
        "Created_Date": log.Created_Date,
        "Room": log.room}
        
    return jsonify(chatlogs_dict)
import random

from flask import request, current_app
from flask_restx import Api, Resource

from api.services.chat import ChatService


rest_api = Api(version="1.0", title="Chatbot API")

@rest_api.route('/api/talk')
class ChatBot(Resource):

    def post(self):
        host = random.choice(current_app.config["TALK_API"])
        bot = current_app.config["BOT_NAME"]

        req_data = request.get_json()
        message = req_data.get("message") if req_data else ""

        data = dict(success=True, message="Please tell something!")
        if message:
            data.update(message=ChatService(host, message, bot).talk())

        return data, 200

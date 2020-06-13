# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from chat.views import *

from blog.views import *
from blog.models import Firebase_module,Pyrebase_module
from django.shortcuts import render,redirect,HttpResponse
class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        try:
            token = self.scope["session"]['token']
        except:
            content = {
            'command': 'redirection',
            }
            return self.send_chat_message(content)

        #try:
        fb =Firebase_module()
        messages = fb.get_a_conversation(data['uid_conv'])
        uid = fb.verify_session_token(token)['uid']
        user = fb.get_name_from_uid(uid)
        content = {
                'command': 'messages',
                'conv': messages,
                'user': user,
            }
        self.send_message(content)
        #except:
        content = {
        'command': 'no_data',
        }
        return self.send_chat_message(content)


       

    def new_message(self, data):
        #try:
        fb =Firebase_module()
        token = self.scope["session"]['token']
      
        uid = fb.verify_session_token(token)['uid']

        fb.add_message_to_conversation(data['message'],data['uuid_conv'],uid)

        uid = data['from']
        user = fb.get_name_from_uid(uid)

        content = {
        'command': 'new_message',
        "Username": fb.get_name_from_uid(uid),
        "message":data['message'],
        "user": user,
         }
        return self.send_chat_message(content)
        #except:
        content = {
        'command': 'redirection',
        }
        return self.send_chat_message(content)
    
   


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
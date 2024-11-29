import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    # Establishes websocket connection
    async def connect(self):
        # extract required info from scope
        self.sender = self.scope['user'].username
        self.recipient = self.scope['url_route']['kwargs']['username']

        # Degines the chat room group
        self.room_group_name = "group_chat"

        # Adds this connection to the chat room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # accepts teh connection
        await self.accept()

    # Handles websocket disconnection
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #handles recieving a message from the websocket client
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # broadcasts the message to the chat room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.sender
            }
        )

    # handles sending message to the websocket client
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
      
      # sends the  message
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))




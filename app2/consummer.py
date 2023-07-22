# import channel 

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class mywebsocketConsummer(WebsocketConsumer): 
    #connect 
    def connect(self):
        print('websocket connect.....')
        print('channel layer...',self.channel_layer)
        print('channel name ...',self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        print("Group name",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept() 
        
    def receive(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        #json data convert to python data 
        data=json.loads(text_data)
        message=data['msg']
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
     #handler function   
    def chat_message(self,event):
        print('event',event) 
        # python data convgert to Json
        self.send(text_data=json.dumps(
            {
                "msg":event['message']
            }
        ))   
        
        
        
    def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)
       
       
class myayncwebsocketConsummer(AsyncWebsocketConsumer):
    
    #connect 
    async def connect(self):
        print('websocket connect.....')
        print('channel layer...',self.channel_layer)
        print('channel name ...',self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        print("Group name",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        self.accept() 
        
    async def receive(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        #json data convert to python data 
        data=json.loads(text_data)
        message=data['msg']
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
     #handler function   
    async def chat_message(self,event):
        print('event',event) 
        # python data convgert to Json
        self.send(text_data=json.dumps(
            {
                "msg":event['message']
            }
        ))   
        
        
            
        
    async def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)       
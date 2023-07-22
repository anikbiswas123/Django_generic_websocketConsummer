# import channel 

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio


class mywebsocketConsummer(WebsocketConsumer):
    
    #connect 
    def connect(self):
        print('websocket conect.....')
        self.accept() 
        
    def receive(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        #self.send(text_data="send to message from client 1") #send data from client
        for i in range(20):
            self.send(text_data=str(i))
            sleep(1)
        
        
    def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)
       
       
class myayncwebsocketConsummer(AsyncWebsocketConsumer):
    
    #connect 
     async def connect(self):
        print('websocket conect.....')
        await self.accept() #accepts the connection
        
     async def receive(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        for i in range(20):
            await self.send(text_data=str(i))
            await asyncio.sleep(1)
            
        
     async def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)       
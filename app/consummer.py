# import channel 

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer


class mywebsocketConsummer(WebsocketConsumer):
    
    #connect 
    def connect(self):
        print('websocket conect.....')
        self.accept() #accepts the connection
        #self.close() # To reject the connection force full connection off kora janno close() method use kora code use kora self.close(code=2545).
        
    def receved(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        self.send(text_data="send to message from client 1") #send data from client
        
    def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)
       
       
class myayncwebsocketConsummer(AsyncWebsocketConsumer):
    
    #connect 
     async def connect(self):
        print('websocket conect.....')
        await self.accept() #accepts the connection
        #self.close() # To reject the connection force full connection off kora janno close() method use kora code use kora self.close(code=2545).
        
     async def receved(self,text_data=None,bytes_data=None):
        print('websocket Received...',text_data)
        await self.send(text_data="send to message from client 1") #send data from client
        
     async def disconnect(self,close_code):
       print("websocket disconnect.....",close_code)       
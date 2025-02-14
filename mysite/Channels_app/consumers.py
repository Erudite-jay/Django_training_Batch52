from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print('WebSocket connected', event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print('Received message', event)
        self.send({
            'type': 'websocket.send',
            'text': 'I got your message',
        })

    def websocket_disconnect(self, event):
        print('WebSocket disconnected', event)
        self.send({
            'type': 'websocket.close',
            'code': 1000,  # Close connection
        })
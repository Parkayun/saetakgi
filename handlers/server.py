# -*- coding:utf-8 -*-
from tornado.escape import json_decode
from tornado.websocket import WebSocketHandler


class ServerIndexHandler(WebSocketHandler):

    saetakgis = {}
    saetakgi_subscribers = {}
    who = ''
    identifier = ''

    def open(self):
    	pass

    def on_close(self):
    	if self.who == 'saetakgi':
        	del ServerIndexHandler.saetakgis[self.identifier]
        elif self.who == 'subscriber':
			ServerIndexHandler.saetakgi_subscribers[self.identifier].remove(self)

    @classmethod
    def write_message_to_subscribers(cls, saetakgi, message):
        for subscriber in cls.saetakgi_subscribers[saetakgi]:
            subscriber.write_message(message)

    def on_message(self, message):
        try:
			data = json_decode(message)
			if data['type'] == 'register':
				if data['who'] == "saetakgi":
					ServerIndexHandler.saetakgis[data['name']] = self
					self.identifier = data['name']

				elif data['who'] == "subscriber":
					ServerIndexHandler.saetakgi_subscribers.setdefault(data['saetakgi'], [])
					ServerIndexHandler.saetakgi_subscribers[data['saetakgi']].append(self)
					self.identifier = data['saetakgi']

				self.who = data['who']
			elif data['type'] == 'activity':
				ServerIndexHandler.write_message_to_subscribers(data['name'], data['what'])

        except (ValueError, KeyError):
            pass

        message = "Done!"
        response = u"Res: " + message
        self.write_message(response)

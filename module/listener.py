import threading
import websocket
import requests
import messages
import json
import time

global func
func=None
def event_message(function_to_decorate=None, event=None):
    global func
    if event == {} : return
    if func != None: func(messages.Message(event['d']))
    if function_to_decorate != None:
        func = function_to_decorate
        try:
            func(messages.Message(event['d']))
        except:
            pass

class Listener:
    def __init__(self, token):
        self.token = token

    def send_json_request(ws, request):
        ws.send(json.dumps(request))

    def recieve_json_response(ws):
        response = ws.recv()
        if response: return json.loads(response)

    def heartbeat(interval, ws):
        time.sleep(0.5)
        while True:
            Listener.send_json_request(ws, { "op": 1, "d": "null" })
            time.sleep(interval)

    def connect(ws,wss_url):
        ws.connect(f'{wss_url}/?v=9&encoding=json')
        event = Listener.recieve_json_response(ws)
        heartbeat_interval = event['d']['heartbeat_interval'] / 1000
        thread = threading.Thread(target=Listener.heartbeat, args=(heartbeat_interval,ws)).start()
        return event

    def identify(self,ws):
        Listener.send_json_request(ws,{"op": 2, "d": {"token": self.token, "intents": 32767, "properties": { "$os": "windows", "$browser": "chrome", "$device": "pc"}}})
        event = Listener.recieve_json_response(ws)
        if (event != None): print("Bot is ready")
        return event

    def listener(ws):
        while True:
            event = Listener.recieve_json_response(ws)
            if event == None : return
            if event["t"] == "MESSAGE_CREATE" : event_message(event=event)

    def start(self):
        global ws
        ws = websocket.WebSocket()
        Hello_event= Listener.connect(ws,"wss://gateway.discord.gg")
        Ready_event = self.identify(ws)
        thread2 = threading.Thread(target=Listener.listener, args=(ws,)).start()

    def stop(self):
        global ws
        ws.close()
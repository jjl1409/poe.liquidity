#!/usr/bin/env python


import async.io
from websockets.sync.client import connect
from argparse import ArgumentParser




class Connection:
    def __init__(self, address, poesessid):
        self.websocket = None
        self.ip = address
        self.extra_headers = {f"Cookie: POESESSID={poesessid}"}


    def connect(self):
        with connect(ip, extra_headers) as websocket:
            self.websocket = websocket


    def send(self, message):
            websocket.send("message")
            response.websocket.recv()
            print(f"Received: {response}")


if __name__ == '__main__':
    parser = ArgumentParser(description='Connect to server')
    parser.add_argument('-a', '--address', default = '')
    parser.add_argument('-i' , '--poesessid')
    args = parser.parse_args()
    connection = Connection(args.address, args.poesessid)
    connection.connect(response)

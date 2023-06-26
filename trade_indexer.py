#!/usr/bin/env python


import requests
import json
from argparse import ArgumentParser

# ADDRESS #
# https://www.pathofexile.com/api/trade/search/Crucible

# POESESSID
# 6d0bbe76e3346cb9d44ec81e0ed54b2a

ex_to_c = {
  "query": {
    "status": {
      "option": "online"
    },
    "have": [
      "exalted"
    ],
    "want": [
      "chaos"
    ]
  },
  "sort": {
    "have": "asc"
  },
  "engine": "new"
}

class Connection:
    def __init__(self, address, poesessid):
        self.websocket = None
        self.ip = address
        self.extra_headers = {f"Cookie: POESESSID={poesessid}"}


    # def connect_to_server(self, ip, extra_headers):
    #     with connect(ip, additional_headers = extra_headers) as websocket:
    #         self.websocket = websocket
    #     print("Connected")


    def post(self, message):
        poesessid = "6d0bbe76e3346cb9d44ec81e0ed54b2a"
        response = requests.post('http://www.pathofexile.com/api/trade/search/Crucible',\
                                 headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}, \
                                 data = ex_to_c, \
                                 cookies = {'POESESSID': poesessid})
        print(response)


if __name__ == '__main__':
    print("Hello")
    parser = ArgumentParser(description='Connect to server')
    parser.add_argument('-a', '--address', default = 'wss://pathofexile.com/api/trade/search/Crucible')
    parser.add_argument('-i' , '--poesessid', default = '6d0bbe76e3346cb9d44ec81e0ed54b2a')
    args = parser.parse_args()
    connection = Connection(args.address, args.poesessid)
    # connection.connect_to_server(connection.ip, connection.extra_headers)
    connection.post(ex_to_c)

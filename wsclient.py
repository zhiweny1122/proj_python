# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:25:59 2018

@author: Administrator
"""

import asyncio
import websockets

async def hello(url):
    async with websockets.connect(url) as webclient:
          await  webclient.send("hello world") 
          print("client waiting ...")
          message = await webclient.recv()
          print("client receive :" + message)

asyncio.get_event_loop().run_until_complete(
        hello('ws://localhost:8765'))
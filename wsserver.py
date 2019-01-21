# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:25:49 2018

@author: Administrator
"""

#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print("server recv" + message)
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
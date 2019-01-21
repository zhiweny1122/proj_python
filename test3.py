# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:11:34 2017

@author: Administrator
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index +=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('aaa'),4)
q.push(Item('abb'),5)        
q.push(Item('abc'),1) 
q.push(Item('ccc'),1) 
q.push(Item('ddd'),2) 

for i in range(0,5):
    print(q.pop().name)
    
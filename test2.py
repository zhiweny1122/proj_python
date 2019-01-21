# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:01:48 2017

@author: Administrator
"""

from collections import deque

def searchline(lines,patten,history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if patten in line:
            yield line, previous_line
        previous_line.append(line)

if __name__ =='__main__':
    with open('sometext.txt') as f:
        for line, prelines in searchline(f,"test",5):
           for pline in prelines:
                print(pline,end='')
           print(line,end='')
        
    print('_'*20)


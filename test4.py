# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:54:28 2017

@author: Administrator
"""

from collections import defaultdict

d =defaultdict(list)
data1 = [
        ('aa',1),
        ('bbb',111),
        ('ccc',11),
        ]

for key,value in data1:
    d[key].append(value)
    
prices = {
        'aaa':100,
        'bb':60,
        'cc':90,
        'dd':60
        }

min_price = min(zip(prices.values(),prices.keys()))
print(min_price)
    
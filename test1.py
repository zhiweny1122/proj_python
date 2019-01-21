# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:14:54 2017

@author: Administrator
"""

record = [
        ('foo',1,3),
        ('bar',"aaa",1),
        ('foo',5,6),
        ('bar',"bb",4),
        ]
def do_foo(x,y):
    print ("foo",x,y)
def do_bar(x,y):
    print("bar",x,y)

for tag,*args in record:
    if tag =='foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
line = "nobody:*:xxx:mm:2012:/var/a:/home/zhiweny"
name,*_,dir1,homedir=line.split(":")
print (name,dir1,homedir)

item1=[1,2,3,4,6,5,10,100]

def sum(item):
    head,*tail=item
    return head+sum(tail) if tail else head

print(sum(item1))


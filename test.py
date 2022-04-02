# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:19:53 2022

@author: Mano
"""





#2question
def value(n):
    d = { 'Square': lambda a : a**2, 
         'Cube': lambda a : a**3, 
         'Squareroot': lambda a : a**(1/2)}       
    sum = 0
    for key in d.keys():
        sum += d[key](n)
    return sum
    
print(value(4))
#3question
fruits = (('Lemon','sour'),('DragonFruit', 'Sweet'),('Grapes','soUr'),('Kiwi','Sour'),('Apples', 'sweet'),('Orange', 'sour'),('Blueberries','sweet'),('Limes','Sour'))
sourFruits=[]
for j in fruits:
    if(j[1].lower()=='sour'):
        sourFruits.append(j[0])
print("Sour Fruits:", sourFruits)
#4question
ls = ['hello' , 'Dear' , 'hOw' , 'You' , 'ARe']
d= []
for s in ls:
    if s[1].isupper():
        d.append(s)
print(d)
#5question
WeightOnEarth = {'John':45, 'Shelly':65, 'Marry':35}
GMoon = 1.622
GEarth = 9.81
dict(map(lambda x : (x, round((WeightOnEarth[x]/GEarth)*GMoon, 2)), WeightOnEarth))
#6question
nameList = ["santa Maria" , "Hello World" , " Merry christmas", "tHank You"]
s = []
for i in nameList:
    a ,b = i.split()
    if a[0].isupper(): 
        s.append(a)
    if b[0].isupper():s.append(b)
print(s)
#7question
def intersection(lst1, lst2): 
    return [item for item in lst1 if item in lst2] 
lst1 = [['a', 'c'], ['d', 'e']] 
lst2 = [['a', 'c'], ['e', 'f'], ['d', 'e']] 
print(intersection(lst1, lst2))
#8question
d= [9,8,7,6,5]
import itertools as it
l=[]
l = it.accumulate(list(enumerate(d)), lambda x,y: (y[0], (x[1]*(x[0]+1) + y[1])/(y[0]+1)))
print(list(map(lambda x: x[1], l)))    
#9question
isbool=["True","FALse","tRUe","tRue","False","faLse"]
list = [x.upper() for x in isbool]
print(list)
#10question
datelists=['17-12-1997','22-04-2011','01-05-1993','19-06-2020']
out=[]
for r in datelists:
    d=r.split("-")
    out.append(d[2])
    print("output",out)
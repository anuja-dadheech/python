#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
print("list: ")
print(adhoc)
a=[]
b=[]
print("1:Numbers greater than 5")
for i in adhoc:
 if i>5:
  print(i)
  a.append(i)
print("2:Numbers less than or equal to 2")
for i in adhoc:
 if i<=2:
  print(i)
  b.append(i)
print("1: ",a)
print("2: ",b)
  






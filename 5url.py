#!.usr/bin/python3
from googlesearch import search
data=input("search--> ")
x=search(data, stop=5)
file=open("urls.txt",'w')
for i in x :
   print(i)
   file.write(i+'\n')

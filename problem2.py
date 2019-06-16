import time
from googlesearch import search
web=input("search--> ")
x=search(web, stop=10)
file=open("f1.txt",'a+')
for i in x :
   print(i)
   time.sleep(1)
   file.write(i+'\n')

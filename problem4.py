#!/usr/bin/python3
import os
import crypt
count=0
string = input()
for i in string:
   if i.isdigit():
     count=1
if count == 0:
   password="hello"+string
   encPass = crypt.crypt(password,"22")
   cmd="useradd -p "+encPass+" "+string
   os.system(cmd)

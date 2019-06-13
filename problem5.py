import datetime
name=input("Enter the name: ")
now=datetime.datetime.now()
if now.hour>=4 and now.hour<12:
 print("Hello,Good Morning")
elif now.hour>=12 and now.hour<17:
 print("Hello,Good Noon")
elif now.hour>=17 and now.hour<20:
 print("Hello,Good Evening")
elif now.hour>=20 and now.hour<24:
 print("Hello,Good Night") 



#!/usr/bin/python3
import datetime
name = input('Enter your name: ')
age = int(input('Enter your age: '))
d=datetime.datetime.now()
years = 95 - age
year=years+d.year
print(f'{name}  will be 95 years old in the year',year)

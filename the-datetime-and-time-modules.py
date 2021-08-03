# This is the Python Essentials 2 LAB 4.5.1.22-the-datetime-and-time-modules
##Write a program that creates a datetime object for November 4, 2020 , 14:53:00.
##The object created should call the strftime method with the appropriate format
##to display the following result:
##2020/11/04 14:53:00
##20/November/04 14:53:00 PM
##Wed, 2020 Nov 04
##Wednesday, 2020 November 04
##Weekday: 3
##Day of the year: 309
##Week number of the year: 44

from datetime import datetime

dt = datetime(2020,11,4,14,53)

print("2020/11/04 14:53:00")
print(dt.strftime("%Y/%m/%d %H:%M:%S"))

print("20/November/04 14:53:00 PM")
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))

print("Wed, 2020 Nov 04")
print(dt.strftime("%a, %Y %b %d"))

print("Wednesday, 2020 November 04")
print(dt.strftime("%A, %Y %B %d"))

print("Weekday: 3")
print(dt.strftime("Weekday: %w"))

print("Day of the year: 309")
print(dt.strftime("Day of the year: %j"))

print("Week number of the year: 44")
print(dt.strftime("Week number of the year: %U"))




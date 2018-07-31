print("Hello")
name = input ("What is your name?")
birthyear = int(input ("What is your year of birth?"))
import datetime
now = datetime.datetime.now()
age = now.year - birthyear
print(age) 

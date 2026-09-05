'''import re 
fullname=input("enter the full name: ")
pattern=r"^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$"                     #fullname
res=re.fullmatch(pattern,fullname)
print("valid full name" if res else "invalid full name")

import re 
fullname=input("enter the full mail: ")
pattern=r"^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$"            #email
res=re.fullmatch(pattern,fullname)
print("valid full email" if res else "invalid full email")

import re 
number=input("enter the number: ")
pattern=r"^(?:\+91|0)?[6-9]\d{9}$"
res=re.fullmatch(pattern,number)                                       #phone number
print("valid phone number" if res else "invalid phone number")

import re 
password=input("enter the password: ")
pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"             
res=re.fullmatch(pattern,password)                                                     #password validation
print("valid password" if res else "invalid password")

import re 
username=input("enter the name: ")
pattern=r"^[a-zA-Z0-9_]{1,15}$"
res=re.fullmatch(pattern,username)                                       #username
print("valid username" if res else "invalid username")'''

import re 
aadhar=input("enter the aadhar: ")
pattern=r"^\d{4} \d{4} \d{4}$"
res=re.fullmatch(pattern,aadhar)                                       #aadhar
print("valid aadhar" if res else "invalid aadhar")

import re 
pancard=input("enter the pancard : ")
pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]$"
res=re.fullmatch(pattern,pancard)                                       #pancard
print("valid pancard" if res else "invalid pancard")




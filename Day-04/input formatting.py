Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int float str list tuple set
x=input()
koushik
x
'koushik'
name=input()
bunny
name
'bunny'
name=input("Enter your name:")
Enter your name:koushik
age=input("Enter your age:")
Enter your age:23
age
'23'
age=int(input("Enter your age:"))
Enter your age:23
age
23
type(age)
<class 'int'>
names=input("Enter the names:")
Enter the names:koushik bunny varshit
names
'koushik bunny varshit'
names.split()
['koushik', 'bunny', 'varshit']
names=input("Enter the names:").split()
Enter the names:koushik bunny varshit
names
['koushik', 'bunny', 'varshit']
names=input("Enter the names:").split()
Enter the names:1 2 3 4 54 5 
names
['1', '2', '3', '4', '54', '5']
map(int,names)
<map object at 0x00000267F4FCCD30>
list(map(int,names))
[1, 2, 3, 4, 54, 5]
values=list(map(int,input().split()))
1 2 34 5 65553
values
[1, 2, 34, 5, 65553]
values=list(map(float,input().split()))
1 2 3454 546.78
values
[1.0, 2.0, 3454.0, 546.78]
names=tuple(input("Enter the names:").split())
Enter the names:koushik reddy bunny 
names
('koushik', 'reddy', 'bunny')
values=tuple(map(float,input().split()))
567 5678 567 
values
(567.0, 5678.0, 567.0)
names=set(input().split())
ytuio yt ui
names
{'ui', 'yt', 'ytuio'}
values=set(map(int,input().split()))
1 2 3 4 
values
{1, 2, 3, 4}
values=set(map(float,input().split()))
1 2 3 4 
values
{1.0, 2.0, 3.0, 4.0}
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input('Enter the email and password:").split()
                     
SyntaxError: unterminated string literal (detected at line 1)
email,password=input("Enter the email and password:").split()
                     
Enter the email and password:kbasika@gmail.com bunny123
emial
                     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    emial
NameError: name 'emial' is not defined. Did you mean: 'email'?
email
                     
'kbasika@gmail.com'
password
                     
'bunny123'
a,b,c=list(map(int,input().split()))
                     
a,b,c=list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c=list(map(int,input().split()))'
a,b,c=list(map(int,input().split()))
                     
1 2 3 
a
                     
1
b
                     
2
c
                     
3
>>> name,marks=input().split()
...                      
koushik 99
>>> name
...                      
'koushik'
>>> marks
...                      
'99'
>>> int(marks)
...                      
99
>>> e=eval(input())
...                      
1
>>> e
...                      
1
>>> e=eval(input())
...                      
12.34
>>> e=eval(input())
...                      
1234.33
>>> e=eval(input())
...                      
[1,2,3,4]
>>> e
...                      
[1, 2, 3, 4]
>>> e=eval(input())
...                      
(1,2,3,4)
>>> e
...                      
(1, 2, 3, 4)
>>> e=eval(input())
...                      
{1,2,3,4}
>>> e
...                      
{1, 2, 3, 4}
>>> e=eval(input())
...                      
{2:2,2:3,2:4}
>>> e
...                      
{2: 4}

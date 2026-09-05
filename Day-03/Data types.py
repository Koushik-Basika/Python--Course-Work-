Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
count =10
count =7
count
7
type(count)
<class 'int'>
price = 99.99
price
99.99
type(price)
<class 'float'>
c= 3+8j
c
(3+8j)
c=4+9j
c
(4+9j)
type(c)
<class 'complex'>
s='codegnan'
type(s)
<class 'str'>
s="code"
type(s)
<class 'str'>
l=[]
l
[]
l= list[]
SyntaxError: invalid syntax
l=list()
type(l)
<class 'list'>
l=[1,2,2,4,4,5,"dfsshjs",78.678,[1,2,3],(1,2)]
l
[1, 2, 2, 4, 4, 5, 'dfsshjs', 78.678, [1, 2, 3], (1, 2)]
type(l)
<class 'list'>
t=()
t=('koushik',1,2,3,4,5.'eged')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> t=('koushik',1,2,3,4,5,'eged')
>>> t
('koushik', 1, 2, 3, 4, 5, 'eged')
>>> type(t)
<class 'tuple'>
>>> s={'koushik','eyyfedy',1,2,3,4,55,55.66)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s={'koushik','eyyfedy',1,2,3,4,55,55.66}
>>> s
{1, 2, 3, 4, 'koushik', 55, 55.66, 'eyyfedy'}
>>> type(s)
<class 'set'>
>>> s={}
>>> s
{}
>>> type(s)
<class 'dict'>
>>> status=none
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    status=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status = none
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    status = none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status = None
>>> type(status)
<class 'NoneType'>
>>> s={1,2,3,4,5,}
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.remove(5)
>>> s
{1, 2, 3, 4, 6}
>>> s= frozenset 9{1,2,3,4]})
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> s= frozenset ({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> s= True
>>> type(s)
<class 'bool'>
>>> s=False
>>> type(s)
<class 'bool'>

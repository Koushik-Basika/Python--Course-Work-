Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
int(a)
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
True
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f=12.3
int(f)
12
complex(f)
(12.3+0j)
str(f)
'12.3'
list(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
bool(f)
True
dict(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
bool(c)
True
dict(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s='code'
int(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'code'
float(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'code'
complex(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e']
tuple(s)
('c', 'o', 'd', 'e')
bool(s)
True
dict(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l= [2:3,3:4,5:6]
SyntaxError: invalid syntax
l = [2,3,4,5,6]
int(l)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[2, 3, 4, 5, 6]'
tuple(l)
(2, 3, 4, 5, 6)
bool(l)
True
dict(l)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
t=(10,20,30)
int(t)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
'(10, 20, 30)'
list(t)
[10, 20, 30]
bool(t)
True
dict(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
s= true
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s= true
NameError: name 'true' is not defined. Did you mean: 'True'?
s=True
int(s)
1
float(s)
1.0
complex(s)
(1+0j)
str(s)
'True'
list(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list(s)
TypeError: 'bool' object is not iterable
tuple(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tuple(s)
TypeError: 'bool' object is not iterable
dict(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(s)
TypeError: 'bool' object is not iterable
s= {2:3,3:4,4:5}
int(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(s)
'{2: 3, 3: 4, 4: 5}'
>>> list(s)
[2, 3, 4]
>>> tuple(s)
(2, 3, 4)
>>> bool(s)
True
>>> dict(s)
{2: 3, 3: 4, 4: 5}
>>> s={"name": "Rohit","age": 21,"course": "Python"}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(s)
"{'name': 'Rohit', 'age': 21, 'course': 'Python'}"
>>> list(s)
['name', 'age', 'course']
>>> tuple(s)
('name', 'age', 'course')
>>> set(s)
{'age', 'name', 'course'}
>>> bool(s)
True

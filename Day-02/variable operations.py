Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a.b,c=10,20,30
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.b,c=10,20,30
ValueError: too many values to unpack (expected 2)
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
>>> a,b=b,a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a,b=b,a
NameError: name 'a' is not defined. Did you mean: 'A'?

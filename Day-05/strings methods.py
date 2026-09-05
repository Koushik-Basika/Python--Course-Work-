Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c='python programming'
len(c)
18
ord('p')
112
ord('a')
97
ord('0')
48
ord('A')
65
chr(65)
'A'
chr(66)
'B'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c='String is immutable'
c
'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
'STRABAGAAngstrromCaf' casefold()
SyntaxError: invalid syntax
'STRABAGAAngstrromCaf'.casefold()
'strabagaangstrromcaf'
c
'String is immutable'
c.center(60,'-')
'--------------------String is immutable---------------------'
c.center(60,'*')
'********************String is immutable*********************'
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
c.ljust(60,'-')
'String is immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------String is immutable'
'12'.zfill(4)
'0012'
'12'.zfill(10)
'0000000012'
'122345'.zfill(5)
'122345'
'456'.zfill(5)
'00456'
c
'String is immutable'
c.find('S')
0
c.find('i')
3
c.find('z')
-1
c.rfind('i')
10
c.rindex('i')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('g')
1
c.count('m')
2
c.count('i')
3
c
'String is immutable'
c.replace('i','0')
'Str0ng 0s 0mmutable'
c.replace('String','Float')
'Float is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
c
'String is immutable'
c.split()
['String', 'is', 'immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String,is,immutable'.split('-')
['String,is,immutable']
'String,is immutable'.rsplit(',')
['String', 'is immutable']
'String,is immutable'.split(',')
['String', 'is immutable']
'String,is immutable'.rsplit('', 1)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    'String,is immutable'.rsplit('', 1)
ValueError: empty separator
'Stringis immutable'.rsplit('', 1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    'Stringis immutable'.rsplit('', 1)
ValueError: empty separator
>>> 'String is immutable'.rsplit('',1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    'String is immutable'.rsplit('',1)
ValueError: empty separator
>>> 'String is immutable'.rsplit(' ',1)
['String is', 'immutable']
>>> s='''
... python
... programming
... lang'''
>>> s
'\npython\nprogramming\nlang'
>>> s.splitlines()
['', 'python', 'programming', 'lang']
>>> ''.join(['', 'python', 'programming', 'lang'])
'pythonprogramminglang'
>>> ' '.join(['', 'python', 'programming', 'lang'])
' python programming lang'
>>> '-'.join(['', 'python', 'programming', 'lang'])
'-python-programming-lang'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> ','.join(['1','2','3'])
'1,2,3'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> c='           Hello     world        '
>>> c
'           Hello     world        '
>>> c.strip()
'Hello     world'
>>> c.lstrip()
'Hello     world        '
>>> c.rstrip()
'           Hello     world'
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'

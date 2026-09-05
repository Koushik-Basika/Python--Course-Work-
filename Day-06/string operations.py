Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string operations
s=''
s
''
s='codegnan'
s
'codegnan'
'codegnan'+'PFS'
'codegnanPFS'
'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'_*_'*20
'_*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*_'
'*'*10
'**********'
s='codegnan'
s=[4]
s[4]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[4]
IndexError: list index out of range
>>> s[4]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[4]
IndexError: list index out of range
>>> s = 'codegnan'
>>> s[4]
'g'
>>> s[-3]
'n'
>>> s[-1]
'n'
>>> s= 'koushik reddy bunny varshit'
>>> s[0]
'k'
>>> s[10]
'd'
>>> s[-12]
'u'
>>> names='koushik karthik jamsine'
>>> s[6]
'k'
>>> s[9]
'e'
>>> s[-12]
'u'
>>> #s [start:end+1:step]=>s[0:len:1]
>>> names[0:5]
'koush'
>>> names[:5]
'koush'
>>> names[12:20]
'hik jams'
>>> names[-1:-8:-1]
'enismaj'
>>> names[::-1]
'enismaj kihtrak kihsuok'
>>> names[::-2]
'eimjkhrkkhuk'
>>> names[::2]
'kuhkkrhkjmie'
>>> 'koushik' in names
True
>>> 'buuny' in names
False
>>> 'karthik' not in names
False

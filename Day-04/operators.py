Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
9//2
4
a%b
0
9%2
1
4**2
16
2**3
8
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
'assissgment operators'
'assissgment operators'
c=10
c=30+c
c
40
c += 10
c
50
c -= 10
c
40
c **= 2
c
1600
c %= 3
c
1
c /= 2
c
0.5
c *= 2
c
1.0
'relational operators'
'relational operators'
n=10
n%2==0
True
n%3==0
False
>>> n%2==0 and n%3==0
False
>>> n%2==0 or n%3==0
True
>>> n%8==0 or n%3==0
False
>>> n
10
>>> n<5
False
>>> not n<5
True
>>> ' membership operators'
' membership operators'
>>> #str list tuple set dict
>>> s='codegnan'
>>> 'e' in s
True
>>> 'z' in s
False
>>> 'f' not in s
True
>>> 'o' not in s
False
>>> l=[1,2,3,4]
>>> 4 in
SyntaxError: invalid syntax
>>> 4 in l
True
>>> 6 in l
False
>>> 8 not in l
True
>>> t=(1,2,3,4)
>>> 1 in t
True
>>> 5 not in t
True
>>> s={1,2,3,5,6,7}
>>> 3 in s
True
>>> 4 not in s
True
>>> 7 not in s
False
>>> d={'name' : 'koushik', 'course' : 'python', 'batch' : 63}
>>> 'name' in d
True
>>> 'python' in d
False
'63' in d
False
'koushik' in d
False
'identity operators'
'identity operators'
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2194269100352
id(m)
2194269098624
l is m
False
n=1
id(n)
140730164771256
l is n
False
n=l
id(n)
2194269100352
l is n
True
l is not m
True
l is not n
False
s={1,2,3,4}
id(s)
2194263827488
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2194263827488
'Bitwise operators'
'Bitwise operators'
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32
8>>3
1
~8
-9
~12
-13
~45
-46
a=10
b=10.3
c='codegnan'
print(a,b,c)
10 10.3 codegnan
print("a value is",a)
a value is 10
print("a value is",a,"| b value is",b,'| c value is ',c)
a value is 10 | b value is 10.3 | c value is  codegnan
print(a,b,c)
10 10.3 codegnan
print(a,b,c,sep='')
1010.3codegnan
print(a,b,c,sep='\n')
10
10.3
codegnan
print(a,b,c,sep='\t')
10	10.3	codegnan
print(a,b,c,sep='\t',end='@')
10	10.3	codegnan@
print(a,b,c,sep='\t',end='\n\n')
10	10.3	codegnan

print(f'a={a} b={b} c={c} ')
a=10 b=10.3 c=codegnan 
print('a=%d b=%f c=%s %(a,b,c))
      
SyntaxError: unterminated string literal (detected at line 1)
print('a=%d b=%f c=%s' %(a,b,c))
      
a=10 b=10.300000 c=codegnan
print('a=%d b=%.2f c=%s' %(a,b,c))
      
a=10 b=10.30 c=codegnan
print(f"a value is {a} | b value is {b} | c value is {c}")
      
a value is 10 | b value is 10.3 | c value is codegnan
print('a={} |b={} |c={}'.format(a,b,c))
      
a=10 |b=10.3 |c=codegnan
print('a={} |b={} |c={}'.format(c,a,b))
      
a=codegnan |b=10 |c=10.3
print('a={1} |b={2} |c={0}'.format(a,b,c))
      
a=10.3 |b=codegnan |c=10

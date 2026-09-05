s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,12,324,9876,34}
s
{1, 2, 3, 324, 4, 34, 12, 9876}
s=set()
s
set()
s.add(1)
a.add(12.3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.add(12.3)
NameError: name 'a' is not defined
s.add(12.3)
s.add(2+4j)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2,3))
s.add({1;2,2:3})
SyntaxError: invalid syntax
s.add(True)
s
{1, 'str', (1, 2, 3), 12.3, (2+4j)}
s.add(False)
s
{False, 1, 'str', (1, 2, 3), 12.3, (2+4j)}
s={1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
l*m
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l*m
TypeError: unsupported operand type(s) for *: 'set' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
#{1{{2}{3}{4}{5}{1,2}{2,3}{3,4}{1,2,3,4}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
a>={1}
True
a>={1,7,9}
False
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
3 in a
True
7 in a
False
8 not in a
True
#set methods
a
{1, 2, 3, 4, 5}
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
b=a
b.add(12)
>>> b
{1, 2, 3, 4, 5, 12}
>>> a
{1, 2, 3, 4, 5, 12}
>>> c=a.copy()
>>> c.add(14)
>>> c
{1, 2, 3, 4, 5, 12, 14}
>>> a
{1, 2, 3, 4, 5, 12}
>>> b
{1, 2, 3, 4, 5, 12}
>>> a.add(123)
>>> a
{1, 2, 3, 4, 5, 123, 12}
>>> a.update({16,17,18})
>>> a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
>>> a.pop()
1
>>> a.pop()
2
>>> a
{3, 4, 5, 12, 16, 17, 18, 123}
>>> a.pop()
3
>>> a.remove(16)
>>> a
{4, 5, 12, 17, 18, 123}
>>> a.remove(12)
>>> a
{4, 5, 17, 18, 123}
>>> a.remove(12)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.remove(12)
KeyError: 12
>>> a.discard(12)
>>> a.discard(5)
>>> a
{4, 17, 18, 123}
>>> a=frozenset({1,12,13,10,18,59,20})
>>> a
frozenset({1, 18, 20, 10, 59, 12, 13})
>>> a.add(12)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'

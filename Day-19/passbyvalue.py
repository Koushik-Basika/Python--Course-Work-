#int float str list tuple set dict bool 

#int float str tuple bool - immutable (values effect)
#list set dict - mutable (same values)

'''def display(n):
    n+=10
    print("inside: ",n)
n=10
display(n)
print("outside: ",n)'''

'''def display(n):
    n+=10.9
    print("inside: ",n)
n=10.5
display(n)
print("outside: ",n)'''

'''def display(n):
    n+=" lang"
    print("inside: ",n)
n="Python"
display(n)
print("outside: ",n)'''

'''def display(n):
    n+=(1,2,3,4)
    print("inside: ",n)
n=(1,2,3)
display(n)
print("outside: ",n)'''

'''def display(n):
    n=False
    print("inside: ",n)
n=True
display(n)
print("outside: ",n)'''

'''def display(n):
    n.append(12)
    print("inside: ",n)
n=[1,2,3,4]
display(n)
print("outside: ",n)'''

def display(n):
    n.add(5)
    print("inside: ",n)
n={1,2,3,4}
display(n)
print("outside: ",n)

'''def display(n):
    n[5]=6
    print("inside: ",n)
n={1:2,3:4}
display(n)
print("outside: ",n)'''




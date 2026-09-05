'''def display(n):
    n=n+10    #local
    print("inside: ",n)
n=10          #global
display(n)
print("outside: ",n)'''

'''def display():
    print('Inside: ',n)
n=10
display()
print('Outside: ',n)'''

'''def display():
    global n
    n=n+10              #dont forget to remove parameters
    print("inside: ",n)
n=10
display()
print("outside: ",n)'''

'''def display():
    global n
    n="PFS"
    print("updated course: ",n)
n="JFS"
display()
print("final course: ",n)'''

'''def display():
    n="JFS"
    def update():
        nonlocal n 
        n="PFS"
        print("updated course: ",n)
    update()
    print("final course: ",n)
display()'''  









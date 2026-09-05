#L
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
'''
#M
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and i<=m) or (i==j and i<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''   
#N
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#O
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
'''
#P
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m or (j==n-1 and i<=m) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Q
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#R
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m or (j==n-1 and i<=m) or (i>=m and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#S
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==m or i==n-1 or (j==0 and i<=m) or (j==n-1 and i>=m) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#T
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#U
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
 '''
 #pyramid pattern
'''
n=int(input()) 
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print() 
'''  
#V 
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''    
#W
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and j<=m) or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#X
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Y
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or (i+j==n-1 and i<=m) or (j==m and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Z
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''   
 
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
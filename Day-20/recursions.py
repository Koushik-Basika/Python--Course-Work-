'''
def func(argv):
    if base_case:
        return
    func(updated argv)
func(para)
'''        
'''
def display(n):
    if n>10:
        return          #correct order 
    print(n,end=" ")
    display(n+1)
display(1) 
'''
'''
def display(n):
    if n>10:
        return          #reverse order 
    display(n+1)
    print(n,end=" ")
display(1) 
'''
'''
def displaysum(n):
    if n==0:
        return 0                  #sum of n numbers
    return n+displaysum(n-1)
print(displaysum(8))    
'''
'''
def productofn(n):
    if n==0:
        return 1                   #product of n numbers or factorial of n numbers 
    return n*productofn(n-1)
print(productofn(7)) 
'''
'''
def display(s,n):
    if n==len(s):
        return                     #string iteration
    print(s[n])
    display(s,n+1)
s="Python Programming"    
display(s,0)
'''
'''
def display(s,n):
    if n>len(s):
        return                     
    print(s[:n])                   
    display(s,n+1)
s="Python Programming"    
display(s,1)
'''
'''
def display(s,n,w):
    if n>len(s)-w:
        return 
    print(s[n:n+w])
    display(s,n+1,w)
s="python programming"
display(s,0,10) 
'''
'''
def display(n):
    if n==0:
        return                     
    display(n//10)                     
    print(n%10)
display(987654)        
'''

def display(n):
    if n==0:
        return 0
    return n%10+display(n//10)
print(display(987654))



#0 1 1 2 3 5 8 13 21 34 
#fibonacci
'''
a=0
b=1
n=10
for i in range(n-1):
    a,b=a,a+b
    print(b)
'''    
       






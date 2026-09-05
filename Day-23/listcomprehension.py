#list comprehension
'''
res=[i for i in range(1,11)]                             #print from 1 to 10 Numbers
print(res)

n=12
res=[i for i in range(1,n+1) if n%i==0]                   #factorial numbers
print(res)

r=[12,23,45,567,123,12,90]
res=[i if i%2==0 else 0 for i in r]                       #even numbers 
print(res)

r=[[12,34,45],[687,474,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]                     # 
print(res)

res=[j for i in range(3) for j in range(1,4)]
print(res)
'''

#set comprehension
'''
res={i for i in range(1,11)}                            #print from 1 to 10 Numbers
print(res)

n=12
res={i for i in range(1,n+1) if n%i==0}                  #factorial numbers
print(res)

r=[12,23,45,567,123,12,90]
res={i if i%2==0 else 0 for i in r}                      #even numbers 
print(res)

r=[[12,34,45],[687,474,123],[34,43,90]]
res={j for i in r for j in i if j%2==0}                   
print(res)

res={j for i in range(3) for j in range(1,4)}
print(res)
'''


'''
l=[int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)                                                                      

names=[input(f"enter the student name - {i+1}: ") for i in range(10)]
print(names)
'''

#dict comprehension
'''
names={input(f"enter the name-{i+1}: "): int(input(f"enter the marks: ")) for i in range(5)}
print(names)

squares={i:i*i for i in range(1,6)}
print(squares)
'''





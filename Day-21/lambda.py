'''
greater=lambda a,b:a if a>b else b
print(greater(12,13))
print(greater(78,90))
print(greater(9,15))
print(greater(45,23))

wish=lambda name:f"welcome to the course {name}"
print(wish("bunny"))
print(wish("srinivas"))
print(wish("ganesh"))

iseven=lambda n:"even" if n%2==0 else "odd"
print(iseven(54))
print(iseven(67))
print(iseven(90))

avg=lambda a,b,c:(a+b+c)/3
print(avg(6,7,8))
print(avg(1,2,3))

domain=lambda mail:(mail.split("@")[-1]).split(".")[0]
print(domain('koushik@codegnan.com'))
print(domain('koushik@gmail.com'))
print(domain('koushik@outlook.com'))
print(domain('koushik@yahoo.com'))

gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(5000))
print(gst(7000))

prices=[5658,4262,7841,8914,1878,249,276]
res=list(map(lambda price: price+price*0.18,prices))
print(res)

names=["bunny","srinivas","ganesh","bharat","varshit","koushik"]
res=list(map(lambda name:name.title(),names))
print(res)

names=("bunny","srinivas","ganesh","bharat","varshit","koushik")
res=tuple(map(lambda name:name.title(),names))
print(res)

names={"bunny","srinivas","ganesh","bharat","varshit","koushik"}
res=set(map(lambda name:name.title(),names))                        
print(res)

prices=[234,456,678,445,784]
res=list(map(lambda price:price-price*0.3,prices))         
print(res)

prices=[234,456,678,400,784]
res=list(filter(lambda price:price>400,prices))           
print(res)

prices=[234,456,678,400,784]
res=list(filter(lambda price:price%2==0,prices))          #even numbers
print(res)

prices=[234,489,678,467,743]
res=list(filter(lambda price:price%2!=0,prices))          #odd numbers
print(res)

names={"bunny","srinivas","ganesh","bharat","varshit","koushik"}
res=list(filter(lambda name:len(name)>5,names))
print(res)


from functools import reduce

l=[3,567,6,24,124,435,462]
res=reduce(lambda sum,i:sum+i,l)
print(res)

names={"bunny","srinivas","ganesh","bharat","varshit","koushik"}
res=reduce(lambda res,i:res+" "+i,names)
print(res)

products={"sugar":60,
           "salt":50,
            "eggs":90,
            "cooking oil":120,
            "bread":45
            }
print(dict(sorted(products.items()))) 
print(dict(sorted(products.items(),reverse=True))) 
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))
'''










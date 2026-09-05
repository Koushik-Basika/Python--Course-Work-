'''
with open("pfs-063.txt","r") as file:                #read
     print(file.read())
     file.seek(0)
     print(file.readline())
     file.seek(0)
     print(file.readlines())
     file.close()

with open("mysql.txt","w") as file:                  #write
     file.write("DDL,DQL,DML")
with open("pfs-063.txt","w") as file:     
     file.write("shifted to branch-5")

with open("pfs-063.txt","a+") as file:                #append
     file.write("tom has girlfriend")   
     file.seek(0)
     print(file.read())

with open("pfs-063.txt","w+") as file:                #write
     file.write("tom has girlfriend")   
     file.seek(0)
     print(file.read())
'''





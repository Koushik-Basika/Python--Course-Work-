class Instagram:
     def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]

     def getpassword(self):
        return self.__password

     def setpassword(self,newpassword):
        self.__password=newpassword

     @property
     def accesspost(self):
        return self._posts

     @accesspost.setter
     def accesspost(self,newpost):
        self._posts.append(newpost)

     def display(self):
        print(self.username,self.__password,self._posts) 


dheeraj=Instagram("dheeraj","dheeraj@133")    
dheeraj.display()
print(dheeraj.username)
print(dheeraj.getpassword())
print(dheeraj.accesspost)

dheeraj.username="bunny"
dheeraj.setpassword("bunny@123")
dheeraj.accesspost="sunrise.png"
dheeraj.accesspost="beach.png"
dheeraj.accesspost="forest.png"

print(dheeraj.username)
print(dheeraj.getpassword())
print(dheeraj.accesspost)











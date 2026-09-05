#multilevel inheritance
class Whatsappv1:
    def messaging(self):
        print("you can message")

class Whatsappv2(Whatsappv1):        
    def calls(self):
        print("you can audio and video calls")

class Whatsappv3(Whatsappv2):
    def status(self):
        print("you can add the status for 24 hrs")        

a=Whatsappv1()
a.messaging()
b=Whatsappv2()
b.messaging()
b.calls()    
c=Whatsappv3()
c.messaging()
c.calls()    
c.status() 


#multiple inheritance 
class Whatsappv1:
    def messaging(self):
        print("you can message")

class Whatsappv2:        
    def calls(self):
        print("you can audio and video calls")

class Whatsappv3(Whatsappv1,Whatsappv2):
    def status(self):
        print("you can add the status for 24 hrs")        

a=Whatsappv1()
a.messaging()
b=Whatsappv2()
b.calls()    
c=Whatsappv3()
c.messaging()
c.calls()    
c.status()

#Hierarchical Inheritance
class Whatsappv1:
    def messaging(self):
        print("you can message")

class Whatsappv2(Whatsappv1):        
    def calls(self):
        print("you can audio and video calls")

class Whatsappv3(Whatsappv1):
    def status(self):
        print("you can add the status for 24 hrs")        

a=Whatsappv1()
a.messaging()
b=Whatsappv2()
b.messaging()
b.calls()    
c=Whatsappv3()
c.messaging()   
c.status()


#Hybrid and multilevel Inheritance
class Whatsappv1:
    def messaging(self):
        print("you can message")

class Whatsappv2:
    def extramessage(self):
        print("you can add emoijs,stickers and gifs")        

class Whatsappv3(Whatsappv1,Whatsappv2):        
    def calls(self):
        print("you can audio and video calls")

class Whatsappv4(Whatsappv3):
    def status(self):
        print("you can add the status for 24 hrs")        

a=Whatsappv1()
a.messaging()
b=Whatsappv2()
b.extramessage()    
c=Whatsappv3()
c.messaging()
c.extramessage()    
c.calls()
d=Whatsappv4()
d.messaging()
d.extramessage()
d.calls()
d.status()



#super method   (one parent)
class Whatsappv1:
    def status(self):
        print("you can add images and videos")

class Whatsappv2(Whatsappv1):
    def status(self):
        super().status()
        print("you can add emoijs,stickers and gifs")        

class Whatsappv3(Whatsappv2):        
    def status(self):
        super().status()
        print("you can like and you can add reaction")

a=Whatsappv3()
a.status()


#multiple parents   (use class instead of super method)
class Whatsappv1:
    def status(self):
        print("you can add images and videos")

class Whatsappv2:
    def status(self):
        print("you can add emoijs,stickers and gifs")        

class Whatsappv3(Whatsappv1,Whatsappv2):        
    def status(self):
        Whatsappv1.status(self)
        Whatsappv2.status(self)
        print("you can like and you can add reaction")

a=Whatsappv3()
a.status()










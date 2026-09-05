from abc import ABC,abstractmethod

class Phonepay(ABC):
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("you can send amount")
    def pin(self):
        print("you need to enter the pin")
    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepay):
    def transaction(self):
        print("you can pay using HDFC bank") 

class UNION(Phonepay):
    def transaction(self):
        print("you can pay using union bank") 


class SBI(Phonepay):
    def transaction(self):
        print("you can pay using sbi bank") 

class AXIS(Phonepay):
    def transaction(self):
        print("you can pay using axis bank") 

class ICIC(Phonepay):
    def transaction(self):
        print("you can pay using icic bank")   


a=HDFC()
a.senderinfo()
a.amount()
a.pin()    
a.transaction()
b=UNION()
b.senderinfo()
b.amount()
b.pin()    
b.transaction()
c=SBI()
c.senderinfo()
c.amount()
c.pin()    
c.transaction()
d=AXIS()
d.senderinfo()
d.amount()
d.pin()    
d.transaction()
e=ICIC()
e.senderinfo()
e.amount()
e.pin()    
e.transaction()






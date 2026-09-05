class Flipkart:
    products={"shirts":100,"saree":890,"makeup":1919}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"hello {self.name}, welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on")  

dheeraj=Flipkart()
dheeraj.userinfo("dheeraj",9012948140,"hyd")
dheeraj.displaydiscount()
dheeraj.display()               #using object -> instance method,class method,static method,class attribute,instance attribute
print(dheeraj.products)
print(dheeraj.name)

Flipkart.displaydiscount()
Flipkart.display()                    #using class -> class method,static method,class attribute
print(Flipkart.products)        



class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"hello {self.name}, welcome to the flipkart")

dheeraj=Flipkart("dheeraj",9012948140)    
koushik=Flipkart("koushik",9046716448)
ganesh=Flipkart("ganesh",74816461941)   




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
dheeraj.display()
koushik=Flipkart() 
koushik.userinfo("koushik",9046716448,"tel")
koushik.displaydiscount()
koushik.display() 
ganesh=Flipkart()
ganesh.userinfo("ganesh",74816461941,"viz") 
ganesh.displaydiscount()  
ganesh.display()     
'''try: 
    #a=int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(l[10])
    #print(10/0)
    print("1"+1)
except Exception as e:                          
    print("Error occured",e)                        
else:                                           
    print("Error free program")
finally:
    print("End of the program")''' 


try: 
   amount=int(input("enter the amount:"))
   balance=5000
   if amount<0:
      raise Exception("Amount needs to be positive")

except Exception as e:                          
    print("Error occured",e)                        
else:                                           
    print("Error free program")
finally:
    print("End of the program")     


      








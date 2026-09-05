#single inheritance
class WhatsappsV1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the Whatsapp - V1 {self.name}!")
    def messaging(self):
        print("You can send messages")

class WhatsappsV2(WhatsappsV1):
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the Whatsapp - V2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

koushik=WhatsappsV1("koushik")
koushik.messaging()

ganesh=WhatsappsV2("ganesh")
ganesh.messaging()
ganesh.calls()


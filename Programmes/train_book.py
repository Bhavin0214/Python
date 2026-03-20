from random import randint

class Train:
    
    def __init__(self, trainNo):
        trainNo = int((input("enter your train no. : ")))
        self.trainNo = trainNo
        
    def book(self, fro, to): 
        print(f"Tickert is boooked in train n0: {self.trainNo} From {fro} to {to}")
        
    def getstatus(self):
        print(f"Train no {self.trainNo} is runniong on time:")
     
    def getprice(self, fro, to):
        print(f"Ticket price of train no {self.trainNo} from {fro} to {to} is {randint(250, 1000)}₹")
        
t = Train(12563)
t.book("jamnagar", "delh")
t.getstatus()
t.getprice("jamnagar", "delh")

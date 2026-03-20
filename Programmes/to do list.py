
class list():
    
    
    def __init__(self, name, status):
        self.name = name
        self.status = status
        L = {name : status} 
        
        def add():
            name = input("enter list name: ")
            status = int(input("status of list enter 1 for done and 0 for not done!"))
            if status == 1:
                L.append(status = "done")
            L.update(name)
        def status():
               
        def delet(self):
            L.remove(self.name, self.status)
       
     
        
while True:
       
    print(f"enter 1 for input list")       
    print(f"enter 2 for input status")       
    print(f"enter 3 for input delet")   

    con = int(input("enter 1/2/3: "))    

    if con == 1:
        list.add()
    elif con== 2:
        list.status()
    elif con==3:
        list.delet()
    else:
        print("invalid input plz try again: ")
        
    show=int(input("enter 0 for show list"))

    if show==0:
        print(f"{L}")
   
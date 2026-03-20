class employee:
    compamny = "nayara"
    name = "bhavin"
    
    def show(self):
        print(f"emplyes name is {self.name} and companay is {self.compamny}")
class coder:   
    lang = "pyhton"     
    def languages(self):

        print(f"employee {self.name} language is {self.lang}")
    
    
    
    
class preogrammer(employee, coder):
    compamny = "nayra infotech"
    
a = employee()
b = preogrammer()
b.compamny
b.show()
b.languages()
import math
import sys
#cowsay also imported
import re 
import csv

postcode_re=(r"\b[A-Za-z0-9]{3,4}\s[A-Za-z0-9]{3}\b")

def main_menu():
    print ("Please select from the following options:\n"
    "1. Log new pet \n"
    "2. Remove pet data\n"
    "3. See health suggestions \n"
    "4. change personal info\n"
    "5. change pet info")

#building pet class with all basic info, species specific will branch off   

class Pet :
    def __init__(self, name,postcode ,age):
        self.name=name
        self.postcode=postcode
        self.age=age
        self.vet=[] #Vet left empty to be assigned later
    
    #check inputs are accurate beore inputting them
        if not name:
            raise ValueError("Missing name")
        if not re.search(postcode_re,postcode):
            raise ValueError("Postcode not valid")
        if age not in [0-30] :
            raise ValueError ("invalid age")
        
    def assign(self, vet):
        #assigns pet to a vet
        self.vet.append(vet) #adds vet to pet data
        vet.add_pet(self) #adds pet to vet data

    def __str__(self):
        return f"{self.name} lives at {self.postcode}"

#sub class cat
class cat(Pet):
    def __init__(self, name, owner, postcode ,age , breed):
        super().__init__(name, postcode, age)
        self.breed=breed
        self.owner=owner
    def __str__(self):
        return super().__str__()
    

#sub class dog 
class dog(Pet):
    def __init__(self, name, owner, postcode ,age ,breed):
        super().__init__(name, postcode ,age)
        self.breed=breed
        self.owner=owner
    def __str__(self):
        return super().__str__()

def log_new():
    name= input("Pet Name:")
    owner= input("Owner:")
    postcode= input("Postcode:")
    age=input("Pet age:")
    pet=Pet(name,owner,postcode,age)
    with open ("Pet_Log.csv") as file:   #open file!! not correct but at least there
        name, owner, pet

class vet:
    #who each pet i sthen assigned to a vet
    def __init__  (self, vet_name, name, owner):
        self.vet_name=vet_name
        self.name=name
        self.owner=owner
        self.assigned_pets=[]  #no assigned pets yet

    def add_pet(self,name):
        if name not in self.assigned_pets :
            self.assigned_pets.append(name)

    def __str__ (self):
        return f"{self.name}belongs to {self.owner} and is under the care of {self.vet_name}"
    





def main():

    #Initiates the main menu and prompts user to select a function
    main_menu()
    if len(sys.argv) < 2:
        print("Please make a selection")
        sys.exit()
   
    n= sys.argv[1]
    if not n:
        print ("No argument provided, please select an option:")

    if n=="1":
        print("hi")

    elif n=="2":
        print("hi")

    elif n=="3":
        print("hi")

    elif n=="4":
        print("hi")

    elif n=="5":
        print("hi")

    else:
        print("Option not recognised")




#testing


# regex


#libraries


#input output
#lambda can be used to calculate pet food weight

#object oriented programming

if __name__=="__main__":
    main()
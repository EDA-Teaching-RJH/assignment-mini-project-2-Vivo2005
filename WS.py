
import os
import sys
import re 
import csv
import cowsay
from faker import Faker


p_re= r"^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$" #regular expression to be used later

square=lambda x: x*x #lamba expression to be used later

#main menu to print when programme begins
def main_menu():
    print ("Please select from the following options:\n"
    "1. Log new pet \n"
    "2. View all pet data\n"
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
        if not re.search(p_re,postcode):
            raise ValueError("Postcode not valid")
        if age not in [0-30] :
            raise ValueError ("invalid age")
        
    def assign(self, vet):
        #assigns pet to a vet
        self.vet.append(vet) #adds vet to pet data
        vet.add_pet(self) #adds pet to vet data

    def health_suggestions(self):
        #suggests health advice based on pet age
        if self.age < 2:
            return f"Feeding suggestion for {self.name} is {square(self.age)} grams of puppy food per day - needs vaccinations and regular vet checkups"
        elif self.age < 8:
            return f"Feeding suggestion for {self.name} is {square(self.age)} grams of adult food per day - regular exercise and balanced diet recommended"
        else:
            return f"Feeding suggestion for {self.name} is {square(self.age)} grams of senior food per day - regular vet checkups and joint supplements may be beneficial"

    def __str__(self):
        return f"{self.name} lives at {self.postcode} and is {self.age} years old"

#sub class cat
class cat(Pet):
    def __init__(self, name, owner, postcode ,age , breed):
        super().__init__(name, postcode, age)
        self.breed=breed
        self.owner=owner

    
    def __str__(self):
        # returns the superior information plus cat specific data
        return f"{super().__str__()} - {self.name} is a cat -{self.breed}- owned by {self.owner}"
    

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


class vet:
    #who each pet i sthen assigned to a vet
    def __init__  (self, vet_name, name, owner):
        self.vet_name=vet_name
        self.name=name
        self.owner=owner
        self.assigned_pets=[]  #no assigned pets yet
    def __str__ (self):
        return f"{self.name}belongs to {self.owner} and is under the care of {self.vet_name}"
    
def add_pet(self,name):
    if name not in self.assigned_pets :
        self.assigned_pets.append(name)

   

#fake code generation
def fake_data():
    fake=Faker()
    if not os.path.exists("pet_log.csv"):
        with open ("pet_log.csv", "w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["name", "owner", "postcode", "age"])
            for _ in range(25):
                writer.writerow([fake.first_name(), fake.name(), fake.postcode(), fake.random_int(min=0, max=30)])
        print("Fake data generated and saved to pet_log.csv")
        
def save_pets(Pet):
    with open("pet_log.csv", "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["name", "owner", "postcode", "age"])
        if isinstance(Pet, cat):
            writer.writerow(["Cat", Pet.name, Pet.owner, Pet.postcode, Pet.age, Pet.breed])
        elif isinstance(Pet, dog):
            writer.writerow(["Dog", Pet.name, Pet.owner, Pet.postcode, Pet.age, Pet.breed])
        else:
            writer.writerow(["Pet", Pet.name, Pet.postcode, Pet.age])

def load_pets():
    pets=[]
    if os.path.exists("pet_log.csv"):
        with open("pet_log.csv", "r") as file:
            reader=csv.reader(file)
            for row in reader:
                pet=Pet(row["name"], row["owner"], row["postcode"], row["age"])
                pets.append(pet)
    return pets

def main():

    #Initiates the main menu and prompts user to select a function
    main_menu()
    if len(sys.argv) < 2:
        print("Please make a selection")
        sys.exit()
   
    n= sys.argv[1]

    if n=="1":
        name= input("Pet Name:")
        owner= input("Owner:")
        postcode= input("Postcode:")
        New_pet=Pet(name,owner,postcode)
        save_pets(New_pet)
        add_pet(New_pet)
        cowsay.yoda(f"{name} logged successfully!")

    elif n=="2":
        fake_data() #generates fake data to print
        print("\nAll pet data:")
        pets=load_pets()
        for p in sorted(pets, key=lambda p: p.name):
            print(p)

    elif n=="3":
        print("\nHealth suggestions:")
        for pet in pets:
            print(f"- {pet.health_suggestions()}")

    elif n=="4":
        print("hi")

    elif n=="5":
        print("hi")

    else:
        print("Option not recognised")
        sys.exit()




#testing


# regex


#libraries


#input output
#lambda can be used to calculate pet food weight

#object oriented programming

if __name__=="__main__":
    main()
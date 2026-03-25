
import os
import sys
import re 
import csv
import cowsay
from faker import Faker
import random


square=lambda x: x*x #lamba expression to be used later

#-----------------------------------------------------------main menu to print when programme begins
def main_menu():
    print ("Please select from the following options:\n"
    "1. Log new pet \n"
    "2. View all pet data\n"
    "3. See health suggestions \n"
    "4. remove pet")
    


#-----------------------------------------------------------class definitions
class Pet :
    def __init__(self, name, zipcode ,age):
       
        self.name=name
        self.zipcode=zipcode
        self.age=age
        self.vet=[] #Vet left empty to be assigned later
    
    #check inputs are accurate beore inputting them
        if not name:
            raise ValueError("Missing name")
        if not age in range(0, 31):
            raise ValueError ("invalid age")
        if not re.search(r"^\d{5}$", zipcode):
            raise ValueError("Invalid zipcode format")
        
    def assign(self, vet):
        #assigns pet to a vet
        self.Vet.append(vet) #adds vet to pet data
        Vet.add_pet(self) #adds pet to vet data

     
    
    def __str__(self):
        return f"{self.name} lives at {self.zipcode} and is {self.age} years old"

#sub class cat
class cat(Pet):
    def __init__(self, name, owner, zipcode ,age , breed):
        super().__init__(name, zipcode, age)
        self.breed=breed
        self.owner=owner

    
    def __str__(self):
        # returns the superior information plus cat specific data
        return f"{super().__str__()} - {self.name} is a cat -{self.breed}- owned by {self.owner}"
    

#sub class dog 
class dog(Pet):
    def __init__(self, name, owner, zipcode ,age ,breed):
        super().__init__(name, zipcode ,age)
        self.breed=breed
        self.owner=owner
    def __str__(self):
        return super().__str__()

class Vet:
    def __init__(self, name):
        self.name=name
        self.pets=[] #list of pets assigned to vet

    def add_pet(self, pet):
        self.pets.append(pet) #adds pet to vet data
        print (self.pets)


#-----------------------------------------------------------fake code generation
def fake_data():
    fake=Faker()
    if not os.path.exists("pet_log.csv"): #fake data for pet log
        with open ("pet_log.csv", "w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["name", "owner", "zipcode", "age"])
            for _ in range(25):
                writer.writerow([fake.first_name(), fake.first_name(), fake.zipcode(), fake.random_int(min=0, max=30)])
        print("Fake data generated and saved to pet_log.csv")
    if not os.path.exists("Vet_log.csv"): #fake data for vet log
        with open ("Vet_log.csv", "w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Dr. Vogel's patients"])
            for _ in range(5):
                writer.writerow([fake.first_name(), "  -  ", random.choice(["cat", "dog"])])
        print("Fake data generated and saved to Vet_log.csv")
    else:
        pass


#-----------------------------------------------------------functions
def log_new():
    name= input("Pet Name:")
    zipcode= input("Zipcode:")
    age=int(input("Pet age:"))
    pet_type= input("Is your pet a cat or dog? (type 'cat' or 'dog'):").lower()
    if pet_type == "cat":
        breed= input("Cat breed:")
        owner= input("Owner name:")
        pet=cat(name, owner, zipcode, age, breed)
    elif pet_type == "dog":
        breed= input("Dog breed:")
        owner= input("Owner name:")
        pet=dog(name, owner, zipcode, age, breed)
    else:
        print("Invalid pet type")
        return None
    return pet



        
def save_pets(Pet):
    with open("pet_log.csv", "a", newline="") as file: #saves pet data to pet log
        writer=csv.writer(file)
        if isinstance(Pet, cat):
            writer.writerow([ Pet.name, Pet.owner, Pet.zipcode, Pet.age,"Cat", Pet.breed])
        elif isinstance(Pet, dog):
            writer.writerow([ Pet.name, Pet.owner, Pet.zipcode, Pet.age,"Dog", Pet.breed])
        else:
            writer.writerow([ Pet.name, Pet.owner, Pet.zipcode, Pet.age,"Pet", "Unknown breed"])
    with open("Vet_log.csv", "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow([Pet.name + " - " + Pet.__class__.__name__]) #adds pet name and type to vet log

def load_pets(): #working well
    pets=[]
    if os.path.exists("pet_log.csv"):
        with open("pet_log.csv", "r") as file:
            reader=csv.reader(file)
            next(reader) #skip names
            for row in reader:
                pets.append(Pet(row[0], row[2], int(row[3]))) #creates pet objects from csv data and adds to list
    return pets

def health_suggestions(name,age):
        #suggests health advice based on pet age
        if age < 2:
            return f"Feeding suggestion for {name} is {square(age)*10+100} grams of puppy/kitten food per day - needs vaccinations and regular vet checkups"
        elif age < 8:
            return f"Feeding suggestion for {name} is {square(age)*10+100} grams of adult food per day - regular exercise and balanced diet recommended"
        else:
            return f"Feeding suggestion for {name} is {square(age)+100} grams of senior food per day - regular vet checkups and joint supplements may be beneficial"




#---------------------------------------------------------------------------------main function to run the programme 
def main():

    #Initiates the main menu and prompts user to select a function
    main_menu()
    if len(sys.argv) < 2:
        print("Please make a selection")
        sys.exit()
   
    n= sys.argv[1]

    if n=="1": #working successfully
        fake_data() #generates fake data to pet and vet 
        pet = log_new()
        save_pets(pet)
        cowsay.tux(f"{pet.name} logged successfully!")

    elif n=="2":
        fake_data() #generates fake data to print
        print("\nAll pet data:")
        pets=load_pets()
        for p in sorted(pets, key=lambda p: p.name):
            print(p)

    elif n=="3":
        n= input("Please input the name of your pet to receive health suggestions:").lower().title()
        with open ("pet_log.csv","r") as file:
            reader= csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == n:
                    print(health_suggestions(row[0],int(row[3])))

    elif n=="4":#to remove pet
        fake_data() 
        rows=[]
        rows_name= input("Please input the name of the pet you wish to remove:").lower().title()
        with open("pet_log.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] != rows_name: 
                    rows.append(row)

        with open("pet_log.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)

            writer.writeheader()
            writer.writerows(rows)
            print(f"{rows_name} has been removed from the pet database.")
        

    else:
        print("Option not recognised")
        sys.exit()


if __name__=="__main__":
    main()   
  
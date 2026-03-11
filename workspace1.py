import math
import sys
#cowsay also imported
import re 
import csv

post_code_re=(r"\b[A-Za-z0-9]{3,4}\s[A-Za-z0-9]{3}\b")

def main_menu():
    print ("Please select from the following options:\n"
    "1. Log new pet \n"
    "2. Remove pet data\n"
    "3. See health suggestions \n"
    "4. change personal info\n"
    "5. change pet info")

#building pet class with all basic info, species specific will branch off   

class Pet :
    def __init__(self, name, owner, postcode ,age):
        self.name=name
        self.owner=owner
        self.postcode=postcode
        self.age=age
    def __str__(self):
        return f"{self.name}is owned by{self.owner},{self.postcode}"

#sub class cat
class cat(Pet):
    def __init__(self, name, owner, postcode ,age , breed):
        super().__init__(name, owner, postcode, age)
        self.breed=breed
    def __str__(self):
        return super().__str__()
    

#sub class dog 
class dog(Pet):
    def __init__(self, name, owner, postcode ,age ,breed):
        super().__init__(name, owner, postcode ,age)
        self.breed=breed
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





def main():
    if len(sys.argv) < 1:
        print("No selection made")
        sys.exit()

#trying to include sys.argv into the selection stage of my code .. failing
   
    n= sys.argv[1]
    if not n:
        print ("No argument provided, please select an option:")

    if n=="1":
        print("hi")

    elif n==2:
        print("hi")

    elif n==3:
        print("hi")

    elif n==4:
        print("hi")

    elif n==5:
        print("hi")

    else:
        print("Option not recognised")




#testing


# regex


#libraries


#input output


#object oriented programming

if __name__=="__main__":
    main()
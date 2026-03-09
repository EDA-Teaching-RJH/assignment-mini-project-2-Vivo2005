import math
import sys
import cowsay #do properly when i can remember how

def main_menu():
    print ("Please select from the following options:\n"
    "1. Log new pet \n"
    "2. Remove pet data\n"
    "3. See health suggestions \n"
    "4. change personal info\n"
    "5. change pet info")

#building pet class with all basic info, species specific will branch off   

class pet :
    def __init__(self, name, owner, postcode ,age):
        self.name=name
        self.owner=owner
        self.postcode=postcode
        self.age=age
    def __str__(self):
        return f"{self.name}is owned by{self.owner},{self.postcode}"

#sub class cat
class cat(pet):
    def __init__(self, name, owner, postcode ,age , breed):
        super().__init__(name, owner, postcode, age)
        self.breed=breed
    def __str__(self):
        return super().__str__()
    

#sub class dog 
class dog(pet):
    def __init__(self, name, owner, postcode ,age ,breed):
        super().__init__(name, owner, postcode ,age)
        self.breed=breed
    def __str__(self):
        return super().__str__()

def log_new():


def main():
    print("Welcome to the National Veterinary Registry")

    x=1
    print ("..Opening profile...")
    while x<4:
        print("...")
        x=x+1


#tying to include sys.argv into the selection stage of my code .. failing
    main_menu()
    n= int(input("pick an option:"))

    if n==1:
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
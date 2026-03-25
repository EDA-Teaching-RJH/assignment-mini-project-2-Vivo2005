from WS import( Pet, cat, dog, Vet)
import os
import pytest
import csv
from WS import (fake_data , log_new, save_pets , load_pets, health_suggestions) 


#-----------------------------------------------------------Pet tests
class test_pet:
    def test_pet_creation(self):
        p = Pet("Buddy", "Alice", "12345", 5)
        assert p.name == "Buddy"
        assert p.owner == "Alice"
        assert p.zipcode == "12345"
        assert p.age == 5

    def test_str(self):
        p = Pet("Buddy", "Alice", "12345", 5)
        assert str(p) == "Buddy lives at 12345 and is 5 years old"

    def test_invalid_name(self):
       with pytest.raises(ValueError, match="Missing name"):
              Pet("", "12345", 5)  #pet only requires name, zipcode and age so owner is not included in this test

    def test_invalid_age(self):
        with pytest.raises(ValueError, match="invalid age"):
            Pet("Buddy", "12345", -1)  #age cannot be negative
        with pytest.raises(ValueError, match="invalid age"):
            Pet("Buddy", "12345", 31)  #age cannot be greater than 30
    
    def test_invalid_zipcode(self):
        with pytest.raises(ValueError, match="Invalid zipcode format"):
            Pet("Buddy", "1234", 5)  #zipcode must be 5 digits
        with pytest.raises(ValueError, match="Invalid zipcode format"):
            Pet("Buddy", "123456", 5)  
        with pytest.raises(ValueError, match="Invalid zipcode format"):
            Pet("Buddy", "abcde", 5)  #zipcode must be a number

class test_cat:
    def test_cat_creation(self):
        c = cat("Whiskers", "Bob", "54321", 3, "Siamese")
        assert c.name == "Whiskers"
        assert c.owner == "Bob"
        assert c.zipcode == "54321"
        assert c.age == 3
        assert c.breed == "Siamese"

    def test_str(self):
        c = cat("Whiskers", "Bob", "54321", 3, "Siamese")
        expected_str = "Whiskers lives at 54321 and is 3 years old - Whiskers is a cat - Siamese - owned by Bob"
        assert str(c) == expected_str

    def test_invalid_breed(self):
        with pytest.raises(ValueError, match="Missing breed"):
            cat("Whiskers", "Bob", "54321", 3, "")  #breed cannot be empty

    def

class test_dog:
    def test_dog_creation(self):
        d = dog("Rex", "Charlie", "67890", 7, "Labrador")
        assert d.name == "Rex"
        assert d.owner == "Charlie"
        assert d.zipcode == "67890"
        assert d.age == 7
        assert d.breed == "Labrador"

    def test_str(self):
        d = dog("Rex", "Charlie", "67890", 7, "Labrador")
        expected_str = "Rex lives at 67890 and is 7 years old"
        assert str(d) == expected_str


#-----------------------------------------------------------Vet tests
class test_vet:
    def test_vet_creation(self):
        v = Vet("Dr. Smith")
        assert v.name == "Dr. Smith"
        assert v.pets == []

    def test_add_pet(self):
        v = Vet("Dr. Smith")
        p = Pet("Buddy", "Alice", "12345", 5)
        v.add_pet(p)
        assert p in v.pets


#-----------------------------------------------------------Other functions tests


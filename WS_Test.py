from WS import( Pet, cat, dog, Vet)
import os
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
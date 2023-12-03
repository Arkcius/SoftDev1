"""
more pettos
Author Ryan Robison
"""
import pets

def main():
    pet = pets.Pet("Hound","Rex",70.0,"Brown")
    print(pet.get_name(),"Weight: ",pet.get_weight())
    pet.feed(1800)
    print(pet.get_name(),"Weight: ",pet.get_weight())
    pet.walk(1.5)
    print(pet.get_name(),"Weight: ",pet.get_weight())

main()
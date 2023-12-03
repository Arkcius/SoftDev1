"""
Purpose fruit stand class
Author: Ryan Robison
"""
class Fruit:
    __slots__ = ["type", "price","count"]
    def __init__(self,type,price):
        self.type = type
        self.price = price  
        self.count = 0

def print_fruit(fruit):
    print(fruit.type,fruit.price)

Apple = Fruit("Apple",1.25)
Pear = Fruit("Pear",1.00)
Strawberry = Fruit("Strawberry",1.75)


      
def add(basket,fruit):
    if fruit == Strawberry.type.lower():
        basket.append(Strawberry)
    elif fruit == Pear.type.lower():
        basket.append(Pear)
    elif fruit == Apple.type.lower():
        basket.append(Apple)
    elif fruit == "":
        pass
    else:
        print("unknown fruit")
    
def price(basket):
    summ = 0.0
    for fruit in basket:
        summ += fruit.price
    return summ

def count(basket,fruit):
    count = 0
    for item in basket:
        if item == fruit:
            count+=1
    return count

def main():
    basket = []
    select = None
    while select != "":
        select = input("Pick a fruit: ")
        add(basket,select.lower())
    for i in range(len(basket)):
        print(basket[i].type)
    prices = price(basket)
    acount = count(basket,Apple)
    pcount = count(basket,Pear)
    scount = count(basket,Strawberry)
    print("Price: ", prices)
    print("Apple Count: ",acount)
    print("Pear Count: ",pcount)
    print("Strawberry Count: ",scount)





main()
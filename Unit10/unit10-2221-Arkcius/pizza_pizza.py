"""
Code pizza class and constructor
Author: Ryan Robison
"""
#toppings class
class Topping:
    #slots and initialize
    __slots__ = ["name","letter","price"]

    def __init__(self,name,letter,price):
        self.name = name
        self.letter = letter
        self.price = price

#pizza class
class Pizza:
    #slots
    __slots__ = ["cheese","veggies","meats",'price']
    #initialize with price using get price to find all topping prices and add them to the base 5
    def __init__(self,cheese,veggies,meats):
        self.cheese = cheese
        self.veggies = veggies
        self.meats = meats
        summ = get_price(cheese) + get_price(meats) + get_price(veggies)
        self.price = 5.00 + summ

#just making some toppings
mozzerlla = Topping("Mozzerlla","m",1.00)
shredded = Topping("Shredded Cheese","s",0.50)
pepperoni = Topping("Pepperoni","p",1.50)
pineapple = Topping("Pineapple","p",1.00)
none = Topping("None","n",0.0)

#the three categories of toppings
MEAT = [pepperoni,none]
CHEESE = [mozzerlla,shredded,none]
VEGGIE = [pineapple,none]

#get price used in pizza init that takes in a category and returns the price summ of all items in it
def get_price(category):
    summ = 0
    #starts sum at 0 and then goes through all elements of the category and adds their .price to it
    for i in range(len(category)):
        summ += category[i].price
    return summ

#prints options for given category
def print_option(category):
    #goes throught every element of the category and prints its name letter and price out
    for element in category:
        print(element.name,"(",element.letter,"): $",element.price,sep = "",end = "\t")
    print()

#order for one category function 
def order(category,name):
    #starts the toppings list
    top = []
    #asks for input
    ord = input("Enter topping letter for " + name +" (0 for options): ")
    #while the input is zero prints the options and asks for input again
    while ord == "0":
        print_option(category)
        ord = input("Enter topping letter for "+name+" (0 for options): ")
    #for all indices of input string compares it to letter for all elements in the category and if they match then adds the topping to the top list
    for i in range(len(ord)):
        for j in range(len(category)):
            if ord[i] == category[j].letter:
                top.append(category[j])
    #returns top
    return top

#orders all toppings for pizza
def orderAll():
    #prints pizza order to signal start of new order
    print("Pizza Order:")
    #calls order for cheese toppings meat toppings and veggie toppings
    cheeses = order(CHEESE,"Cheese")
    meats = order(MEAT,"Meat")
    veggies = order(VEGGIE,"Veggie")
    #returns a pizza using above topping lists
    return Pizza(cheeses,veggies,meats)

#prints pizza
def print_pizza(pizza):
    print("One Pizza with ",end = "")
    #goes through each element of pizza cheese meat and veggie and prints out their names
    for i in range(len(pizza.cheese)):
        if pizza.cheese[i].letter != "n":
            print(pizza.cheese[i].name,end = " ")
    for i in range(len(pizza.meats)):
        if pizza.meats[i].letter != "n":
            print(pizza.meats[i].name,end = " ")
    for i in range(len(pizza.veggies)):
        if pizza.veggies[i].letter != "n":
            print(pizza.veggies[i].name,end = "")
    #then prints the price of said pizza
    print(":", pizza.price)

#main
def main():
    pizza1 = orderAll()
    pizza2 = orderAll()
    print_pizza(pizza1)
    print_pizza(pizza2)
    print("Total Due: ",pizza1.price+pizza2.price)

main()
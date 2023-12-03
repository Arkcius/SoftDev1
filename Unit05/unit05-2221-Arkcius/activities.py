"""
Purpose to make activities
Author: Ryan Robison
"""

def numbers():
    total_sum = 0
    while True:
        string = input("Enter Filename: ")
        if string == "":
            break
        with open(string) as file:
            summ = 0
            for line in file:
                try:
                    num = float(line)
                except:
                    num = 0
                summ += num
        total_sum += summ
        print("Sum of numbers: ",summ)
    print("Total Sum: ",total_sum)

def numbers2():
    total_sum = 0
    while True:
        string = input("Enter Filename: ")
        if string == "":
            break
        try:
            with open(string) as file:
                summ = 0
                for line in file:
                    num = float(line)
                    summ += num
            total_sum += summ
            print("Sum of numbers: ",summ)
        except:
            print("File not found at",string)
    print("Total Sum: ",total_sum)


def numbers3():
    total_sum = 0
    while True:
        string = input("Enter Filename: ")
        if string == "":
            break
        try:
            with open(string) as file:
                summ = 0
                for line in file:
                    num = float(line)
                    summ += num
            total_sum += summ
            print("Sum of numbers: ",summ)
        except ValueError:
            print("File contains non Numeric Data")
        except FileNotFoundError:
            print("File not found at",string)
    print("Total Sum: ",total_sum)


def numbers4():
    total_sum = 0
    while True:
        string = input("Enter Filename: ")
        if string == "":
            break
        try:
            with open(string) as file:
                summ = 0
                for line in file:
                    try:
                        num = float(line)
                        summ += num
                    except ValueError:
                        print("File contains non Numeric Data:",line)
            total_sum += summ
            print("Sum of numbers: ",summ)
        except FileNotFoundError:
            print("File not found at",string)
    print("Total Sum: ",total_sum)

def division():
    errors = 0
    while True:
        num = input("Enter Numerator: ")
        deno = input("Enter Denominator: ")
        if num == "" or deno == "":
            break
        try:
            answer=float(num)/float(deno)
            print("Result: ",answer)
        except ValueError as ve:
            errors +=1
            if errors >= 3:
                raise ve
            print("Non-Numeric value Entered")
        except ZeroDivisionError as ze:
            errors +=1
            if errors >= 3:
                raise ze
            print("Can't Divide by zero")

def password():
    password = input("Enter Password between 10-20 Characters: ")
    num = len(password)
    if num < 10 or num > 20:
        raise ValueError("Invalid Password")
    else:
        confirm = input("Enter Pasword again: ")
        if confirm == password:
            print("They Match")
            return password
        else:
            raise ValueError("Passwords Must Match")

def exponent(base,power):
    total = base**power
    print(total)
    

def main():
    exponent(2,4)
    #password()
    division()
    numbers4()
    #numbers3()
    #numbers2()
    #numbers()

main()
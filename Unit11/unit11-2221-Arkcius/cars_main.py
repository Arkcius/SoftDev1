"""
Cars main
Ryan Robison
"""
import cars

def main():
    car1 = cars.Car("ABCD1234", "Ford", "Escape", 2018)
    car1.print_car()
    car2 = cars.Car("QFGH5678", "Buick", "Encore", 2016)
    car2.print_car()

    print()
    car1.filler_up(7)
    car1.print_car()
    car2.filler_up(20)  # Challenge will cap fuel at 15
    car2.print_car()

    print()
    car1.drive(180)
    car1.print_car()
    car2.drive(480)  # Challenge will cap mileage at 450
    car2.print_car()

    print()
    print(str(car1))
    print(car2)

    print()
    car3 = cars.Car("QFGH5678","Ford","Model T",1908)
    print(car1,"==",car2,":",car1 == car2)
    print(car1,"==",car3,":",car1 == car3)
    print(car2,"==",car3,":",car2 == car3)

    car4 = cars.Car("EJKL9012","Pontiac","Firebird",1967)
    car5 = cars.Car("BNOP3456","Chevrolet","Camaro",1966)
    car_list = [car1, car2, car3, car4, car5]
    car_list.sort()
    print(car_list)

    car_set = set(car_list)
    print(car_set)

main()
class Car:
    country = 'Japan'
    year = 2030
    name = 'Prius'
    
    def __init__(self, country, year, name):
        self.country = country
        self.year = year
        self.name = name
    
    def print_name(self):
        print('Print name実行')
        print(f"{self.name}、{self.country}、{self.year}")
    
# print(Car.country)
# print(Car.year)

my_car = Car("Cebu", 2000, "hikaru")
# print(my_car.year)
# print(my_car.country)
my_car.print_name()


class Oreo:    
    number = 0   
    
    def __init__(self, number):
        self.number = number
                
    def caluculater(self, number):
        for _ in range(number):
            number *= number
        return number
    
my_oreo = Oreo(5)
print(my_oreo.caluculater(2))
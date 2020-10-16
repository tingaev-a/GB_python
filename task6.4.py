class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        pass
    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turn  {direction}')

    def show_speed(self):
        print(f'Speed, {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Alert!!! Speed ,{self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Alert!!! Speed ,{self.speed}')

class PoliceCar(Car):
    pass


car1 = TownCar(90, 'red', 'Audi', False)
car2 = SportCar(190, 'black', 'AMG', False)
car3 = WorkCar(40, 'green', 'ZAZ', False)
car4 = PoliceCar(140, 'blue', 'Chevrolet', True)
car5 = TownCar(50, 'white', 'BMW', True)

car1.show_speed()
car2.go()
car2.turn('Right')
car2.stop()
print(car3.name)
print(car4.name)

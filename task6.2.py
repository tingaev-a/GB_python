class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def mass(self, depth):
        density = 25
        mass = self._width * self._lenght * depth * density / 1000
        return mass

road1 = Road(20, 5000)
print(road1.mass(5))

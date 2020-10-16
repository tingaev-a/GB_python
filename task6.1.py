from time import sleep


class TrafficLight:
    def __init__(self):
        pass

    def running(self):
        while True:
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("gren")
            sleep(4)

light = TrafficLight()
light.running()
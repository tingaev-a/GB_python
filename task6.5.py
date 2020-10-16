class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start rendering')


class Pen(Stationery):
    def draw(self):
        print('writes pen')


class Pencil(Stationery):
    def draw(self):
        print('Pencil id drows')


class Handle(Stationery):
    def draw(self):
        print('Handle is paints')


pen1 = Pen('Parker')
pencil1 = Pencil('Koh-i-noor')
handle1 = Handle('Zebra')

pen1.draw()
pencil1.draw()
handle1.draw()
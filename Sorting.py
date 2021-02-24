import pygame as pg


class Rectangle():
    def __init__(self, pos_y):
        self.y = 20 * pos_y
        self.x = 0
        self.size_x = elements[pos_y]
        self.size_y = 20
        self.colour = (0, 0, 0)

    def drawing(self, pos_y, colour):
        pg.draw.rect(window, colour, (0, pos_y * 20, elements[pos_y], 20))


    def change(self, first, second):
        self.drawing(first, (0, 255, 255))
        self.drawing(second, (0, 255, 255))


        pg.display.update()
        pg.time.delay(500)


        if elements[first] > elements[second]:
            self.drawing(first, (0, 255, 0))
            self.drawing(second, (0, 255, 0))


            pg.display.update()
            pg.time.delay(500)


            self.drawing(first, (255, 255, 255))
            self.drawing(second, (255, 255, 255))


            pg.display.update()
            pg.time.delay(500)


            elements[first], elements[second] = elements[second], elements[first]


            self.drawing(first, (0, 255, 0))
            self.drawing(second, (0, 255, 0))


            pg.display.update()
            pg.time.delay(500)
        else:
            self.drawing(first, (255, 0, 0))
            self.drawing(second, (255, 0, 0))


            pg.display.update()
            pg.time.delay(500)


        self.drawing(first, (0, 0, 0))
        self.drawing(second, (0, 0, 0))
        

        pg.display.update()
        pg.time.delay(500)


elements = list(map(int, input().split()))
rectangles = dict()
sort = False


pg.init()
window = pg.display.set_mode((1000, len(elements) * 20))
window.fill((255, 255, 255))


for i in range(len(elements)):
    rectangles[i] = Rectangle(i)
    rectangles[i].drawing(i, (0, 0, 0))


while True:
    if sort != True:
        for i in range(len(elements) - 1):
            for j in range(len(elements) - 1 - i):
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()
                rectangles[j].change(j, j + 1)


        sort = True
    else:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


    
class Rectangle():
    def __init__(self,longsize,shortsize):
        self.longsize = longsize
        self.shortsize = shortsize
    def calculateArea(self):
        self.area=self.longsize*self.shortsize
        print(self.area)
Rectangle(10,20).calculateArea()


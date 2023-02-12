class vehicle():
    #Attributes
    brand=None
    color=None
    wheels=0
    doors=0
    #Constructor
    def __init__(self,brand,color,wheels,doors):
        self.brand=brand
        self.color=color
        self.doors=doors
        self.wheels=wheels
    #Getter
    def getBrand(self):
        return self.brand
    def getColor(self):
        return self.color
    def getWheels(self):
        return self.wheels
    def getDoors(self):
        return self.doors
    #Setter
    def setBrand(self,brand):
        self.brand=brand
    def setColor(self,color):
        self.color=color
    def setWheels(self,wheels):
        self.wheels=wheels
    def setDoors(self,doors):
        self.doors=doors
    #Override
    def __str__(self):
        return f'El coche es de la marca {self.brand}, tiene {self.doors} puertas, es de color' \
               f' {self.color} y tiene {self.wheels} ruedas'
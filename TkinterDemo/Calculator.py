import tkinter

class Calculator:

    def calculate_cost(self, price_per_gallon: float, mpgs: float, distance: float):
        gallonsUsed = distance / mpgs
        return gallonsUsed * price_per_gallon

    def getPPG(self):
        return self.__pricePerGallon

    def getMPGs(self):
        return self.__mpgs

    def getDistance(self):
        return self.__distance

    def setPPG(self, value):
        self.__pricePerGallon=value

    def setMPGs(self, value):
        self.__mpgs= value

    def setDistance(self, value):
        self.__distance = value
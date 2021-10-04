import random
from abc import ABC, abstractmethod


class Colour(ABC):
    @abstractmethod
    def props(self):
        pass


class RGB(Colour): 
    def __init__(self):
        self.type="RGB"
        self.red = random.randrange(0,255,1) 
        self.blue = random.randrange(0,255,1) 
        self.green = random.randrange(0,255,1) 
    def props(self):
        data = {
            "type": self.type,
            "red": self.red,
            "blue": self.blue,
            "green": self.green
        } 
        return data

class HSL(Colour):  
    def __init__(self):
        self.type="HSL"
        self.hue = random.randrange(0,360,1) 
        self.saturation = random.randrange(0,100,1) 
        self.lightness = random.randrange(0,100,1) 
    def props(self):
        data = {
            "type": self.type,
            "hue": self.hue,
            "saturation": self.saturation,
            "lightness": self.lightness
        } 
        return data

class BGRB(Colour):  
    def __init__(self):
        self.type="BGRB"
        self.red = random.randrange(0,10000,1) 
        self.blue = random.randrange(0,10000,1) 
        self.green = random.randrange(0,10000,1) 
    def props(self):
        data = {
            "type": self.type,
            "red": self.red,
            "blue": self.blue,
            "green": self.green
        } 
        return data

##Colour List
colour_array=[RGB, HSL]#, BGRB]  

def random_colour():
    return colour_array[random.randint(0,len(colour_array)-1)]()
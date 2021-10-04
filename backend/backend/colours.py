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
        self.saturation = random.randrange(0,1000,1) 
        self.lightness = random.randrange(0,1000,1) 
    def props(self):
        data = {
            "type": self.type,
            "red": self.hue,
            "blue": self.saturation,
            "green": self.lightness
        } 
        return data

##Colour List
colour_array=[RGB, HSL]  

def random_colour(x=random.randrange(0,len(colour_array))):
    if x >= len(colour_array):
        raise Exception
    
    return colour_array[x]()
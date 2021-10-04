import random
from abc import ABC, abstractmethod


class Colour(ABC):
    @abstractmethod
    def props(self):
        pass


class RGB(Colour): 
    def __init__(self, red=0, blue=0, green=0):
        self.type="RGB"
        self.red =  random.randrange(0,255,1) if red == 0 else red    
        self.blue = random.randrange(0,255,1) if blue == 0 else blue    
        self.green = random.randrange(0,255,1) if green == 0 else green    
    def props(self):
        data = {
            "type": self.type,
            "red": self.red,
            "blue": self.blue,
            "green": self.green
        } 
        return data

class HSL(Colour):  
    def __init__(self, hue=0, saturation=0, lightness=0):
        self.type="HSL"
        self.hue = random.randrange(0,360,1) if hue == 0 else hue
        self.saturation = random.randrange(0,100,1) if saturation == 0 else saturation
        self.lightness = random.randrange(0,100,1) if lightness == 0 else lightness
    def props(self):
        data = {
            "type": self.type,
            "hue": self.hue,
            "saturation": self.saturation,
            "lightness": self.lightness
        } 
        return data

class BGRB(Colour):  
    def __init__(self, red=0, blue=0, green=0):
        self.type="BGRB"
        self.red =  random.randrange(0,10000,1) if red == 0 else red    
        self.blue = random.randrange(0,10000,1) if blue == 0 else blue    
        self.green = random.randrange(0,10000,1) if green == 0 else green 
    def props(self):
        data = {
            "type": self.type,
            "red": self.red,
            "blue": self.blue,
            "green": self.green
        } 
        return data

##Colour List
colour_array=[RGB, HSL, BGRB]  

def random_colour():
    return colour_array[random.randint(0,len(colour_array)-1)]()
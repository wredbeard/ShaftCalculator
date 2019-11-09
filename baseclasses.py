import math

class cylinder(object):
    
    feature_type = "cylinder"

    def __init__(self, diameter = 0, length = 0):
        self.diameter = diameter
        self.length = length
        self._start_z = 0.00

    def get_volume(self):
        area = ((self.diameter / 2.0) ** 2) * math.pi
        volume = area * self.length
        return volume
    
    def end_z(self):
        return self._start_z + self.length


class shaft(object):

    def __init__(self):
        self.features = []
        self.density = 0.284 # Steel = .284 lb / cu in.
        self.weight = 0
        
    def get_volume(self):
    
    	volume = 0.00
    	
    	for feature in self.features:
    		volume = volume + feature.get_volume()
    		
    	return volume
    
    def calculate_weight(self):
        volume = self.get_volume()
        self.weight = volume * self.density

        return



    def get_length(self):
    
    	length = 0
    	
    	for feature in self.features:
    		length = length + feature.length
    		
    	return length

    def add_feature(self, feature):	
        feature._start_z = self.get_length
        self.features.append(feature)
        self.calculate_weight()






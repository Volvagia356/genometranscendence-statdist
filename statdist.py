from collections import OrderedDict

class StatDist():
    def __init__(self,attributes,points):
        self.attributes=OrderedDict()
        for attr in attributes:
            self.attributes[attr]=0
        self.total_points=points
        self.points=points
    
    def adj_point(self,attr,amount):
        if (amount>=0 and amount<=self.points) or (amount<0 and abs(amount)<=self.attributes[attr]):
            self.attributes[attr]+=amount
            self.points-=amount
        else:
            raise StatPointError

class StatPointError(Exception):
    pass
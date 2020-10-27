import pdb

from utils.weather import Weather


class TempretureComparetor():
    def __init__(self, variance: int):
        self.variance=variance

    def compare(self,w1: Weather,w2: Weather):
        return abs(w1.temp_c-w2.temp_c)

    def compare_temprature(self,w1: Weather,w2: Weather):
        if(self.compare(w1,w2)<=self.variance):
            return True
        else:
            raise Exception("WTF temperature difference is too huge Sue NDTV for false Weather Reporting!")

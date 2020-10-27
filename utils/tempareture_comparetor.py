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
            raise Exception(f"WTF temperature reported by NDTV is {w1.temp_c} and openweatherapi is {w2.temp_c} and it is too huge Shouldn't NDTV be sued for false Weather Reporting!")

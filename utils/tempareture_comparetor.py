import logging
import pdb
import utils.custom_logger as cl
from utils.custom_exception import CustomException
from utils.weather import Weather


class TempretureComparetor():
    log = cl.customLogger(logging.INFO)
    def __init__(self, variance: int):
        self.variance=variance

    def compare(self,w1: Weather,w2: Weather):
        return abs(w1.temp_c-w2.temp_c)

    def compare_temprature(self,w1: Weather,w2: Weather):
        self.log.info(f"performing comparision of temperature between {w1.temp_c} and {w2.temp_c} with the referance temp of {self.variance}")
        if(self.compare(w1,w2)<=self.variance):
            return True
        else:
            raise CustomException(f"WTF temperature reported by NDTV is {w1.temp_c} and openweatherapi is {w2.temp_c} and it is too huge Shouldn't NDTV be sued for false Weather Reporting!")

import logging
import pdb
from traceback import print_stack
import json

import utils.custom_logger as cl
import requests

class ApiHelper():
    log = cl.customLogger(logging.DEBUG)

    def get(self,uri,params=None,header=None):
        try:
            if not header:
                header={"Content-Type": "application/json"}
            res=requests.get(url=uri,params=params,headers=header)
            if(res.status_code==200):
                self.log.info("the requested url "+ uri+ "with params "+str(params)+" is successful ")
                return res
            else:
                self.log.info("the requested url is not successful please check the url and params "+ uri +" " +str(params))
        except:
            self.log.error("unable to perform get call for url "+uri+ " params "+ str(params))


    def post(self,uri,params=None,header=None):
        try:
            if not header:
                header={"Content-Type": "application/json"}
            res=requests.get(url=uri,json=params,headers=header)
            if(res.status_code==200):
                self.log.info("the requested url is not successful")
                return res
            else:
                self.log.info("the requested url is not successful please check the url and params "+ uri +" " +params)
        except:
            self.log.error("unable to perform get call for url "+uri+ " params "+ params)



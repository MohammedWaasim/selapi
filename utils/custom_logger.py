import inspect
import logging
import pdb

def customLogger(logLevel=logging.DEBUG):
    #Get the name of the class/method from where this method is called
    loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)
    #by default, log all messages
    logger.setLevel(logging.DEBUG)
    fileHandler=logging.FileHandler("automation.log",mode="a")
    fileHandler.setLevel(logLevel)
    #formatter = logging.Formatter("%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
     #                             datefmt='%m/%d/%Y %I:%M:%S %p')
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
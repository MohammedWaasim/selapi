import csv
import yaml
def getCSVData(fileName):
    rows=[]
    dataFile=open(fileName,"r")
    reader=csv.reader(dataFile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows

def getYamlData(filename, ):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data




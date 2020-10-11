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

def getYamlData(filename, section='default_data'):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    if section.__contains__('default'):
        return data['default_data']
    return data[section]




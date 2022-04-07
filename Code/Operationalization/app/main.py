import json
import time

from settings import get_enviroment_variables
from aws import Aws

name = "elian"

def csv():
    import csv
    file = open("../../Data/Raw/room_temp_rawdata.csv")
    reader = csv.reader(file)
    aws = Aws(get_enviroment_variables(name)) 
    for row in reader:
        print(row)
        room = {
            'Timestamp':row[0], 
            'Temperature_Celsius':row[1],
            'Relative_Humidity':row[2]
        }
        aws.publish(row, 1)
    file.close()
    aws.disconnect()

def main():
    csv()


if __name__ == '__main__':
    main()

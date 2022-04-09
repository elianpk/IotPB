import json
import time

from settings import get_enviroment_variables
from aws import Aws
from aws_shadow import Aws_Shadow

name = "shadow"

def csv():
    import csv
    file = open("../../Data/Raw/room_temp_rawdata.csv")
    reader = csv.reader(file)
    aws = Aws_Shadow(get_enviroment_variables(name)) 
    next(reader)
    for row in reader:
        print(row)
        room = {
            'Timestamp':row[0], 
            'Temperature_Celsius': float(row[1]),
            'Relative_Humidity':float(row[2])
        }
        aws.publish(room, 1)
        air_conditioner_actuator(aws, float(row[1]))
    file.close()
    aws.disconnect()


def air_conditioner_actuator(aws, temperature):
    message = {
          "state": {
            "reported": {
              "power": True if temperature >= 21 else False
            }
          }
        }
        
    aws.publish(message, 1)


def main():
    csv()


if __name__ == '__main__':
    main()

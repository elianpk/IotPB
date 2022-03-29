import json
import time

from settings import get_enviroment_variables
from aws import Aws

def csv():
    import csv
    file = open("../../Data/Raw/japanese_room_temp_rawdata.csv")
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()

def main():
    aws = Aws(get_enviroment_variables("shadow")) 
    message = {"temperatura": 25.00}
    aws.publish(message, 1)

    csv()


if __name__ == '__main__':
    main()

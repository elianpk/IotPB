from settings import get_enviroment_variables
from aws import Aws
from shadow_control import air_conditioner_actuator

name = "elian"

def csv():
    import csv
    file = open("../../Data/Raw/room_temp_rawdata.csv")
    reader = csv.reader(file)
    aws = Aws(get_enviroment_variables(name))
    next(reader)
    for row in reader:
        print(row)
        room = {
            'Timestamp':row[0], 
            'Temperature_Celsius': float(row[1]),
            'Relative_Humidity':float(row[2])
        }
        #aws.publish(room, 1)
        if float(row[1]) >= 21:
            air_conditioner_actuator('on')
        else:
            air_conditioner_actuator('off')

    file.close()
    aws.disconnect()



def main():
    csv()


if __name__ == '__main__':
    main()

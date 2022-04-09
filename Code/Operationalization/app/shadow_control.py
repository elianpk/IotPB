from aws_shadow import Aws_Shadow as Aws
from settings import get_enviroment_variables

def air_conditioner_actuator(aws, temperature):
    message = {
          "state": {
              "power": True if temperature >= 21 else False
          }
        }
        
    aws.publish(message, 1)
    aws.disconnect()

aws = Aws(get_enviroment_variables("shadow")) 
air_conditioner_actuator(aws, 21)
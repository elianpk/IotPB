from aws import Aws
from settings import get_enviroment_variables

def air_conditioner_actuator(aws, temperature):
    message = {
          "state": {
            "desired": {
              "power": True if temperature >= 21 else False
            }
          }
        }
        
    aws.device_shadow_publish(message, 1)

aws = Aws(get_enviroment_variables("shadow")) 
air_conditioner_actuator(aws, 21)
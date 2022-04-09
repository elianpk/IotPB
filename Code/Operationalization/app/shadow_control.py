from aws import Aws
from settings import get_shadow_enviroment_variables

import sys

def air_conditioner_actuator(desired_state):
    aws = Aws(get_shadow_enviroment_variables("elian")) 
    if desired_state:
        message = {
            "state": {
                "desired": {
                    "power": True if desired_state == 'on' else False
                }
            }
        }
        aws.publish(message, 1)
        aws.disconnect()
    else:
        print('Selecione um estado para o atuador')

desired_state = sys.argv[1] if len(sys.argv) > 1 else None
air_conditioner_actuator(desired_state)
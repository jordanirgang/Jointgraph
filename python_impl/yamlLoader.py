import os
import yaml
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Load

cwd = os.getcwd()
yaml_file = os.path.join(str(cwd),"resources/network_config.yaml")

stream = open(yaml_file, 'r')
dictionary = yaml.load(stream,Loader=yaml.Loader)
#print(dictionary['server']['port'])

URDF_LOCATION = dictionary['urdf']['location']

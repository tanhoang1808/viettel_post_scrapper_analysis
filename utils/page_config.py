import yaml

import os


def readPageConfig(target_environment='dev'):

    config = initYamlConfig()
    environment_runtime = config[target_environment]
    
    
    return environment_runtime

def initYamlConfig(file_path='config/environment_config.yaml'):
    with open(file_path,'r') as file:
        config = yaml.safe_load(file)
        return config
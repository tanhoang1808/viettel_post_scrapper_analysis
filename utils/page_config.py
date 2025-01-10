import yaml
from yaml_config import InitYamlConfig


def readPageConfig(target_environment):

    config = InitYamlConfig()
    environment_runtime = config['target'][target_environment]
    
    
    return environment_runtime



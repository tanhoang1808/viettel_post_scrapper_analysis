import yaml
from utils.yaml_config import InitYamlConfig


def readPageConfig(target_environment='dev',use_thread='False'):

    config = InitYamlConfig()
    # config['use_thread'] = use_thread
    # config['target'] = config['target'][target_environment]


   
    return config



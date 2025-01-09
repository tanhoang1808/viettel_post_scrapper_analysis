import yaml

import os
load_dotenv('config/page_config.env')


def readPageConfig(target_environment='dev'):

    config = initYamlConfig()
    environment_runtime = config[target_environment]
    print(environment_runtime)

    base_url = environment_runtime['base_url']
    page_max = environment_runtime['page_max']
    start_page = environment_runtime['start_page']
    end_page =  environment_runtime['end_page']
     

    if not base_url or not page_max:
    
        
        raise Exception("Can not find properties base_url or page_max")

    return {
        base_url : base_url,
        page_max : page_max,
        start_page : start_page,
        end_page : end_page
    }


def initYamlConfig(file_path='utils/environment_config.yaml'):
    with open(file_path,'r') as file:
        config = yaml.safe_load(file)
        return config
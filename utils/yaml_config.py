import yaml


def InitYamlConfig(file_path='config/environment_config.yaml'):
    with open(file_path,'r') as file:
        config = yaml.safe_load(file)
        return config


def OverrideConfig(config,args):
    if args.target:
        config['target'] = config['target'][args.target]
    if args.thread is not None:
        config['use_thread'] = args.thread
    if args.target is None:
        config['target'] = config['target']['dev']
    return config
from yaml import load


def load_config(conf_file):

    try:
        conf = open(conf_file, "r")
        data = load(conf)
        return data, f'Successfully load config from {conf_file}.'
    except FileNotFoundError:
        return None, f'Could not load file from {conf_file}.'

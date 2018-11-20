from yaml import load


def load_config(conf_file):

    conf = open(conf_file, "r") 
    data = load(conf)
    return data
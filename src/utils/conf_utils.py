from yaml import load


def conf_dict(conf_file):

    conf = open(conf_file, "r") 
    data = load(conf)
    return data
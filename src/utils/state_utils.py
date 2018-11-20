from yaml import dump
from yaml import Dumper

def save_state(state, path):

    print(dump(state))
    #f = open(path + "current_state.yaml", "w")
    #f.write(dump(state))


    
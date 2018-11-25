import datetime
import os


def get_state_file(path):

    now = datetime.datetime.now()
    n_d = now.day
    n_mo = now.month
    n_y = now.year

    state_filename = f'{n_d}_{n_mo}_{n_y}_current_state.yml'
    state_fullpath = path + state_filename

    if not os.path.isfile(state_fullpath):
        f = open(state_fullpath, 'w+')
    else:
        f = open(state_fullpath, 'a+')

    f.close()

    return state_fullpath


def add_timestamp(state_filepath):

    f = open(state_filepath, 'a+')

    now = datetime.datetime.now()

    n_d = now.day
    n_mo = now.month
    n_y = now.year

    n_h = now.hour
    n_mi = now.minute
    n_s = now.second

    f.write(f'# created on {n_d}:{n_mo}:{n_y} {n_h}:{n_mi}:{n_s}{os.linesep}')
    f.write(f'{os.linesep}')
    f.close()


def save_state(song_state, path):

    f = open(path, 'a+')

    filepath = song_state['filepath']
    # - filename:
    f.write(f'- "{filepath}":{os.linesep}')

    # inside filename
    for key, value in song_state.items():

        f.write(f'    {key}: "{value}"{os.linesep}')

    f.write(f'{os.linesep}')

    f.close()

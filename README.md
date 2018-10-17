# Tau

Little helper for formatting music directory on your PC.

When you accumulate your music directory with files from different sources, over time that directory gets really messy and disorganized.

Here is my solution to make formatting more easier and automatic.

## How it works

State of directory is represented with yaml notation.
You can print it in terminal or save it to file.

Changing data in directory must follow this steps:

1. Creating yaml file with current state
2. Calculating new state
3. [optional] Manually correcting yaml file of new state if there are some errors
4. Applying new state on your directory

### Current state

```python
pipenv run python current_state.py args
```

Args:

* dp - path to music directory
* yp - [optional] path where yaml file will be saved. If it's not set then it will be printed in terminal

### New State

```python
pipenv run python new_state.py args
```

Args:

* yc - path to yaml file of current state
* yp - [optional] path where new yaml file will be saved.
* at - [optional] data which we'll try to correct. default value is all. list of values:

      * all
      * artwork[XxY] - XxY are dimensions of cover
      * lyrics
      * format[320]

### Applying state

```python
pipenv run python fix_me.py args
```

Args:

* yp - path to yaml file
* dp - path to music directory
* nd - path to new music directory. if you don't want to change existing music directory and want to create new directory.

## TODO

* Find song metadata(artist, song, album year,...) based on current metadata(including directory where audio file is stored)
* Convert audio files to desired format(320kbs,flac,...)
* Find album covers
* Add lyrics to audio files in metadata
* Format musib library to desired tree format
* Change info/metadata to desired encoding
* Create GUI app for this lib
* Make generic api interface to be able to add more apis from different sites for informations.
* Make conf file instead command line arguments

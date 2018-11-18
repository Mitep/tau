import mutagen.easyid3
import mutagen.flac
import mutagen.aac
from phrydy import MediaFile
from phrydy.mediafile import FileTypeError

def get_tags(filename):

        try:
                file = MediaFile(filename)
                tags = {}
                for i in file.fields():
                        if i == 'art':
                                continue
                        tags[i] = getattr(file, i)
                return tags
        except FileTypeError:
                print('Unsuported file format')
                return {}
        '''
        type = filename.split('.')[-1]
        if type.lower() == 'mp3':
                return get_tag_dict(mutagen.easyid3.EasyID3(filename))
        elif type.lower() == 'flac':
                return get_tag_dict(mutagen.flac.FLAC(filename))
        elif type.lower() == 'aac':
                return get_tag_dict(mutagen.aac.AAC(filename))

def get_tag_dict(file):
        tags = {}
        for key in file.keys():
                tags[key] = file.get(key)
        return tags
        '''
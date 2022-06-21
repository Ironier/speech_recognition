import os
from config import Config
conf = Config()
wav_path = conf.get("FILE_DATA").wav_path
label_file = conf.get("FILE_DATA").label_file

with open(label_file, 'w', encoding='utf8') as out:
    for (dirpath, dirnames, filenames) in os.walk(wav_path):
            for filename in filenames:
                if filename.endswith('.trn'):
                    with open(wav_path+filename) as f:
                        path = f.readline().strip('\n')
                    with open(wav_path+path,encoding='utf8') as f:
                        path = f.readline().strip('\n')
                    out.write('{} {}\n'.format(filename[:-8],path))

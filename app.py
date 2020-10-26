import easyocr
import glob
import os
from itertools import groupby

base_path = '/root/.EasyOCR'
output_path = '/app/output/'
txt_ext = '.txt'
replacable = 'l 먼문사 '

reader = easyocr.Reader(['ko', 'en'])

def get_path (path, filename, ext):
    return f'{path}{key}{ext}'

files = list(sorted(filter(lambda x: x != 'model', os.listdir(base_path))))
for key, group in groupby(files, lambda x: x.split('.')[0]):
    for item in group:
        print(item)

        f_name = get_path(output_path, key, txt_ext)
        with open(f_name, 'a+') as output:
            result = reader.readtext(f'{base_path}/{item}', detail=0)
            output.write(' '.join(result).replace(replacable, '') + '\n')
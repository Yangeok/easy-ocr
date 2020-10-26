import easyocr
import glob
import os
from itertools import groupby

base_path = '/root/.EasyOCR'
replacable = 'l 먼문사 '

reader = easyocr.Reader(['ko', 'en'])

files = list(sorted(filter(lambda x: x != 'model', os.listdir(base_path))))
for key, group in groupby(files, lambda x: x.split('.')[0]):
    for item in group:
        print(item)
        with open(f'/app/output/{key}.txt', 'a+') as output:
            result = reader.readtext(f'{base_path}/{item}', detail=0)
            output.write(' '.join(result).replace(replacable, '') + '\n')
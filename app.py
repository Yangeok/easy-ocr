import easyocr
import glob
import os

base_path = '/root/.EasyOCR'
reader = easyocr.Reader(['ko', 'en'])
files = glob.glob(f'{base_path}/*.png')
print(files)

new_files = list(filter(lambda x: x != 'model', os.listdir(base_path)))

group = list(map(lambda x: x.split('.')[0], new_files))
print(group)

for i in range(len(files)):
    f_name = files[i]
    result = reader.readtext(f_name, detail=0)
    f_path = f_name.split('/')[3]
    print(f_name)
    print(f_path)
    with open(f'/app/output/{f_path}.txt', 'w') as output:
        output.write(' '.join(result) + '\n')
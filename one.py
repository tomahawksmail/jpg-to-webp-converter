from webptools import cwebp
import os
import pathlib
import glob
path = r'C:\Users\smoke\Downloads\Newfolder'
desktop = pathlib.Path(path)


end = '.webp'
def obxodFile(path):

    i = 0
    for file in desktop.rglob("*"):
        if file.is_file():
            newfile = str(file).split('.')[0]
            newfile = newfile + end
            cwebp(input_image=file, output_image=newfile, option="-q 80", logging="-v")
            i+=1
            print(i, newfile, 'done')



obxodFile(path)

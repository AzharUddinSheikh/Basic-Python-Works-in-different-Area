from pathlib import Path
from zipfile import ZipFile

# if no file then it ll create one
'''with ZipFile("files.zip", "w") as zip:
    for path in Path("direcory").rglob("*.*"):
        zip.write(path)'''


with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("direcory/workingwithzipfile.py")
    print(info.file_size)
    print(info.compress_size)

    # zip.extractall("extract")
    '''above method not only created extract dir but also create all those file which is in dircory dir inside extract '''
# its gives a all file

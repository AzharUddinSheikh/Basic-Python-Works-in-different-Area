from pathlib import Path

# for absolute path
# Path("C:\\User\\azhar\\Desktop")
# Path(r"C:\User\azhar\Desktop")

#  for mac or lennox
# Path("/user/loal/bin")

# path object that represent current path
# Path()

# going through a path from current
# Path("Mosh Python/app")

# combining path as a string or by path

# Path() / Path("Mosh Python/ecommerce")
# Path() / "Mosh Python"/"ecommerce"/ "__init__.py"

# path has a class method called home which return the home directory

# Path.home()

path = Path("workingwithpath.py")
print(path.exists())  # to check file or directory exists or not
print(path.is_file())  # tthis ll check path represt a file or not
print(path.is_dir())  # to check its represent directory or not
print(path.name)  # to give filename to this path
print(path.stem)  # its remove .py from name of the file
print(path.suffix)  # its shows only .py from name of the file
print(path.parent)  # its shows in which directory its loaded
'''if you replace .txt inplace of file.txt then it automatically added stem __init__'''
paths = (path.with_name("file.txt")
         )  # we can use this to create a new path object based on this existing path but only change the name and the extension of the file
print(paths)
print(paths.absolute())  # for abs value of this path

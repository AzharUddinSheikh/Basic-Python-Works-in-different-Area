from pathlib import Path

path = Path("workingwithdirectory.py")

'''path.exists() # to existence of the dir or file 
path.mkdir() # to make the dir 
path.rmdir() # to remove or del dir 
path.rename("workingwithdir.py") # to rename '''

(path.iterdir())  # its show a generator object we can use it when dir have million of files and want us to do specific

'''above thing is iterable we can use it for loop '''
# to convert into list we use list comphrehension
paths = [p for p in path.iterdir()]
'''if above path is dir then its show something strange result posixpath object 
because above we imported is a base class for two different classes posixpath and windows path for mac you see posix path and for window you ll see windowpath object '''

'''lets say we need a file or dir from that thing '''

paths = [p for p in path.iterdir() if p.is_dir()]

# searching for all file *.* or searching for *.py only py file

py_file = [p for p in path.glob("*.py")]
# print(py_file) it ll show only py file in a list

# for r glob method or recursive method to get all py file
py_file = [p for p in path.rglob("*.py")]

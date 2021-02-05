from pathlib import Path
from time import ctime

path = Path("workingwithfile.py")

'''path.exists
path.rename("workingwithfiles.py")
path.unlink() # to del
'''
(path.stat())
# that return information about this file

(ctime(path.stat().st_ctime))
# human redable data

(path.read_bytes())
# above method didnt get it
(path.read_text())
# above method ll return the whole file content in string format

'''but above method we can also use with open("__inti__.py", "r") as file:
                                        '''
path.write_text("")

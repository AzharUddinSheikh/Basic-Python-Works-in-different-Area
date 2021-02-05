# not working

#  with this module we can spot a child process
#  A process is basically an instance of running program so we can run other program
import subprocess

# for running external program
# if you want to run the python script other than current module then

# print(dir(subprocess))

# these method below are helper method to create an instance of the p open class


'''
subprocess.call
subprocess.check_output
subprocess.check_call
subprocess.Popen'''

# there is a better approach for this
result = subprocess.run(args=["ls", "-l"])

print(type(result))

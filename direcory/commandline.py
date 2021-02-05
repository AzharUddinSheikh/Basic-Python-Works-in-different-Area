import sys

x = (sys.argv)
print(x)
#  if you print x you get something like ['c:\\Users\\azhar\\Desktop\\Few Method\\MOSH PYTHON\\direcory\\commandline.py']

if len(sys.argv) == 1:
    print("usage: python3 commandline.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

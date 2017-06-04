from sys import argv
from os.path import exists
script,from_file,to_file = argv
out_file = open(to_file,'w')
out_file.truncate()
in_file = open(from_file).read()
print out_file.write(in_file)
out_file.close()

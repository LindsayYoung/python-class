# This script assumes the file is in the same folder
file_name = 'sample.txt'

# this opens the file, it takes the file name as an argument
txt = open(file_name)

# this reads your file
print txt.read()

# it is a good idea to explicitly close your file
txt.close()
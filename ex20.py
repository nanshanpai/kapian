#from sys import argv
#script, filename = argv

#print("First let's print the whole file:")
#file = open(filename)
#stuf = file.read()

#print(stuf)

#print("Now let's rewind, kind of like a tape.")
#print("Let's print three lines:")
#file.seek(0)
#for r in range(1, 4):
    
 #   print(file.readline())

from sys import argv
 
script, input_file = argv
 
def print_all(f):
     print(f.read())
	 
def rewind(f):
    f.seek(0)
	
def print_a_line(line_count, f):
    print(line_count, f.readline())
 
current_file = open(input_file)
 
print("First let's print the whole file:\n")
 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
 
rewind(current_file)
 
print("Let's print three lines:")
 
current_line = 1
print_a_line(current_line, current_file)
 
current_line = current_line + 1
print_a_line(current_line, current_file)
 
current_line = current_line + 1
print_a_line(current_line, current_file)
 
 

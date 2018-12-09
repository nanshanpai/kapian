#自己编写的部分

#from sys import argv
#script, fromfile, tofile = argv
#text1 = open(fromfile)
#file1 = text1.read()


#text2 = open(tofile, 'w')
#text2.write(file1)
#print("the input file is %d bytes long" % len(file1))
#text1.close
#text2.close

# 书中呈现
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist？ %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# 打开的是文件参数，读取的是数据，写入的也是数据，关闭的是打开赋值给程序中的参数 而非真实的文件，也即是全是参数在行动而非实际文件
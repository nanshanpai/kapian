# 输入参数并打开文件赋值给变量
from sys import argv
script, filename = argv
txt = open(filename)
# 打印 打开的文件名
print("Here's your file %r:" % filename)
print(txt.read())
# 用input 直接输入文件，input可以传送文件，
#两种输入的区别在于 argv 输入一系列参数，而input 一次输入一个文件
print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print(txt_again.read())



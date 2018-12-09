# 笨办法学python 中途 总结

# 按照给三个月之前的自己教python的方式
# 启动
# 安装
我用的是windows，而笨办法用的也是2.7

1. 所以要准备的是以python2.7的软件，安装windows的power shell,配置python的路径，就可以运行了，据说linux he mac的系统更好，有条件可以安装linux系统，准备硬盘空间，启动U盘，下载liux程序安装即可，关键是要重新学习linux下的shell 命令，shell是一种命令行的外壳程序和脚本环境，就是能运行和执行python的环境。

2. 输出 print "hello word" 开始，print 可以输出字符，函数，变量，运算，等各种变量
如print "hello word" print 7*8  ,print "hello word %r" % bianliang 字符格式化的程序
print " wo had a little 'lamp'."  print """afafasfa
adfjalfjal
dfajfla
adfadfaf
"""
a = ""
b = ""
print a+b 

3. 算术运算
print 4*5+5/6+6/2+6*2+3%6  print 4.0/5  注意浮点运算，和取余数和四舍五入 的运算。
print a+b 变量运算

4. 输入一 a=raw_input() raw_input('>')  raw_input(a)  
输入变量和用户进行交互，从而获得用户的数据
如print "how old are you %d" % raw_input()
print " my oled is %r " % raw_input()

   输入二 from sys import argv
     script, aa, bb = argv
例子如从一个文件拷贝另外一个文件的内容

5. 文本操控 
导入可以用  from sys import argv script, aa,bb= argv
number = file.read()
number = file.open()
number = open(file,'w')
file.line()

 文件的读取 写入 行数 开启 关闭的命令

6. 函数 
  def aaa(a,b):
      print a+b
     print a*b
    return a*b+a+b
def aaa(a):
    print a/5
    return a*5
定义函数名称格式 名称括号，变量，冒号，运行的变量操作


----------------------------

程序列表的总结
print " hello world"
print " ok 'ok'"
# -*- coding: utf-8 -*-
IDLE
Power sell
# "dddd"
+ - * / % < > <= >=    a+_
round() word[2:5]  len(s) word.append(s) word[:] = []
print " %r %d %s %"  % (a,b,....,z)
\\  \' \'' \a \b \f\n \N \r \t \ uxxxx \ uxxxxxxxx \ v \ooo \ xhh
raw_input()

from sys import argv script,first ,second, third = argv

open(filename)  txt.read() open(filename, 'w')  txt.close txt.truncate()

def funtion(args):  缩进
int()
return

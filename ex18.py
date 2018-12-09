#def print_d(arg1 ,arg2):
 #   print("arg1: %r , arg2: %r " %(arg1, arg2))

#def print_s(arg1):
 #   print("arg1: %r" % arg1)
	
#def print_all(*args):
##    arg1, arg2 = args
 #   print("arg1: %r , arg2: %r " %(arg1, arg2))
	
	
#print_d(1, 2)
#print_s(3)
#print_all(5, 6)


#this one is like your scriptss with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
	
# ok ,that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
	
# this just takes one arguments
def print_one(arg1):
    print("arg1: %r" % arg1)
	
# this one takes no arguments
def print_none():
    print("I got nothin'.")
	
	
print_two("Zen","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# *args arg1, arg2....= args 参数赋值，
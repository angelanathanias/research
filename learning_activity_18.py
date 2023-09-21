# change this code
mystring = "hello"
myfloat = 10.0
myint = 20


# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
  
# Write a Python program that takes the text from the New Zealand national anthem "God Defend New Zealand", 
# then covert it using the swapcase() method. The program must display this on the screen. 
quote = "God Defend New Zealand"
print(quote)
print("\nIn swapcase:")
print(quote.swapcase())

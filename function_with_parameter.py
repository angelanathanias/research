# Function2.py
#
# @ author: A. N. Other
# date: September 2016
 
def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))
 
 
# creating and setting a counter
counter = 0
print("Testing my second user defined function...\n\n")
 
counter += 1
# invoking the function
show_hello(counter)
 
counter += 1
# invoking the function again
show_hello(counter)

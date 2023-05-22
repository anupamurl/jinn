import time


search = "a,b,c,d"

def my_function(arg):
 print(arg)


for data in search.split(","):
    my_function(data)
    time.sleep(3)

# SuperFastPython.com
# example of a parallel for loop with the Thread class
from threading import Thread
import turtle
import time

# Initializing the turtle

n =[]
n2 =[]

 
# execute a task
def task():
    # add your work here...
    n.append(2)
tic = time.perf_counter()  
for a in range(32244):
    task()
    #task2(t2,i)
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
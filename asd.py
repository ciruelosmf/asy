# SuperFastPython.com
# example of a parallel for loop with the Thread class
from threading import Thread
import turtle
import time

# Initializing the turtle

 
n2 =[]

 
 
 
    #print(f'.done {t}')

def task2(i):
    # add your work here...
    n2.append(i)
  

# protect the entry point
if __name__ == '__main__':
    tic = time.perf_counter()  
    threads = [Thread(target=task2, args=(i,)) for i in range(32244)]
    toc = time.perf_counter()
    # start all threads
    for thread in threads:
        thread.start()
    
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"Downloaded the tutorial 2 in {toc - tic:0.4f} seconds")



    # report that all tasks are completed
    print('Done')
    print('Done')
    
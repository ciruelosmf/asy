# SuperFastPython.com
# example of a parallel for loop with the Thread class
from threading import Thread
import turtle
    
# Initializing the turtle

  
  



# execute a task
def task(i):
    # add your work here...
    r = 50 + (i*2)
    t.circle(r)
    #print(f'.done {t}')

# protect the entry point
if __name__ == '__main__':
    global t
    t = turtle.Turtle()
    # create all tasks
    threads = [Thread(target=task, args=(i,)) for i in range(4)]
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    # report that all tasks are completed
    print('Done')

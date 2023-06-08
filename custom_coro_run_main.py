print( )
import asyncio
import math
import copy
import time
ga = [1,2,3,4]
 

g = 0

async def task_coroutine():
    global g 
    print(2222, g, "g")
    g += 1
    time.sleep(13)
    await asyncio.sleep(13)
#coro = task_coroutine()
# create a task from a coroutine
#asyncio.run(coro)
#task = asyncio.create_task(task_coroutine())
#print(task)

# define a coroutine
async def custom_coro():
    print(2,"custom")
 

    await asyncio.sleep(2)

async def custom_coro2():
    print(3)

    await asyncio.sleep(1)


# main coroutine
async def main():
    print("pre1 task")

    task = asyncio.create_task(task_coroutine())
    print("pre2 task")
    task
    print(task)
    print("post task")

    await task_coroutine()
    print("post task2")

    await custom_coro()
    await custom_coro2()
 
# start the coroutine program

asyncio.run(main())
print()
class Node:
    gf = 22
    def __init__(self, val = 0, l = None,r = None) -> None:
        self.val = val
        self.l = l
        self.r = r
   
  
print()
#loop = asyncio.new_event_loop()
# report defaults of the loop
#print(loop)
 
 








    

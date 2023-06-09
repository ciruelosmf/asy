print( )
import asyncio
import math
import copy
ga = [1,2,3,4]

d = 3






# define a coroutine
async def make_tea():
    await asyncio.sleep(1)    
    boil_water()
    print("take cups")
    print("insert tea leaves in cup")
    await asyncio.sleep(1)
    print("insert water in cup")
    print(3)
    await asyncio.sleep(1)





async def boil_water():
    print("start kettle")
    await asyncio.sleep(2)  
    print("waiting boil")
    await asyncio.sleep(4)  
    print("water boiled ")
    await asyncio.sleep(2)






# main coroutine
async def main():

    task_1 = asyncio.create_task(boil_water())   
    await asyncio.sleep(1)
     
    print("take cups")
    await asyncio.sleep(1)

    print("insert tea leaves in cup")
    await asyncio.sleep(1)
    await asyncio.gather(task_1)
    print("insert water in cup")
    await asyncio.sleep(1)

    print("end")
 





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

 
 








    

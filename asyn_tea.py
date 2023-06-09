print( )
import asyncio
import math
import copy
ga = [1,2,3,4]
 


# SuperFastPython.com
# check the type of a coroutine
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
    await asyncio.sleep(1)  
    print("waiting boil")
    await asyncio.sleep(2)  
    print("water boiled ")
    await asyncio.sleep(1)






# main coroutine
async def main():
    # execute my custom coroutine
    await make_tea()

 





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

 
 








    

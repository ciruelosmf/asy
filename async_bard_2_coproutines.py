import asyncio
print()

async def print_number_one():
  for i in range(32):
    await asyncio.sleep(2)
    print(4)

async def print_number_two():
  for i in range(32):
    await asyncio.sleep(1)
    print(1)

async def main():
  await asyncio.gather(print_number_one(), print_number_two())
  print("-")

if __name__ == "__main__":
 
  asyncio.run(main())
  print("--")




print()




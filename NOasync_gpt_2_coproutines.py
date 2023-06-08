 
import time

start_time = time.time()
second = 0
second2 = 0

def print_number(number, duration, t = None):
    global second
    global second2

    for i in range(duration):
        if t == "t1":
            print(number, "num", second, "--secon")
            second +=1 
            time.sleep(1)
        elif t == "t2":
            print(number, "num", second2, "--secon")
            second2 +=1 
            time.sleep(1)
def main():
    print("create_task(print_number(1, ")

    task1 = print_number(1, 11,"t1")
    print("create_task(print_number(1, t1")
    task2 = print_number(22222, 11,"t2")
    print("gather2")

    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    time.sleep(1)  # Wait for 1 second
    
    print("end")

main()
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
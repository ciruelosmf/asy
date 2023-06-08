from threading import Thread
import time

j = (2,3,5,[])
print(j[-1].append(4))
print(j )

# execute a task
def task(value):
    # add your work here...
    value = value * 2
    # all done
    print(f'.done {value}')

# protect the entry point
if __name__ == '__main__':


    # create all tasks
    tic = time.perf_counter()        
    threads = [Thread(target=task, args=(i,)) for i in range(20)]






    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    # report that all tasks are completed
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

    tic2 = time.perf_counter()        
    threads2 = [i*2 for i in range(20)]
    toc2 = time.perf_counter()
    print(f"Downloaded the tutorial2 in {toc2 - tic2:0.6f} seconds")

    print('Done')
import concurrent.futures
# execute a task




def task(value):
# add your work here...
    value = 1 + value
    return value




# protect the entry point
if __name__ == '__main__':
# create the pool with the default number of workers
    with concurrent.futures.ThreadPoolExecutor() as exe:
# issue some tasks and collect futures
        futures = [exe.submit(task, i) for i in range(50)]
# handle results as tasks are completed
        for future in concurrent.futures.as_completed(futures):
            print(f'>got {future.result}')
        # issue one task for each call to the function
        for result in exe.map(task, range(50)):
            print(f'>got {result}')
        # report that all tasks are completed
    print('Done')
"""
::Multi-Threading in Python Demo::

Multi-Threading is advantageous when we are trying to perform
multiple I/O operations in parallel.

In case for CPU heavy parallel operations, we'd actually
want to use Multi-Processing.
"""

# import threading
import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    """Sleep function"""
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)
    return f"DONE for {seconds}"


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    # secs = [1,2,3,4,5]
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    # print(results)
    for result in results:
        print(result)
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # secs = [1,2,3,4,5]
#     secs = [5,4,3,2,1]
#     results = [executor.submit(do_something, sec) for sec in secs]
#     # print(results)
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#     # results = [executor.submit(do_something, _) for _ in range(1,6)]
#     # # print(results)
#     # for f in concurrent.futures.as_completed(results):
#     #     print(f.result())

# # do_something()
# # do_something()
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f"Time Take: {round(finish-start,3)} second(s)")

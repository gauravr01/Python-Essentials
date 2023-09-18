# Concurrency and asynchronous programming are important concepts 
# in Python for handling tasks efficiently and effectively. Here's a detailed
#  explanation of the modules and concepts related to concurrency and asynchronous
#  programming in Python:

# Threading:
# The threading module in Python allows you to create and manage threads.
#  Threads are lightweight execution units that can run concurrently within a
#  single process. They are useful for parallelizing tasks and performing I/O-bound 
# operations. However, due to the Global Interpreter Lock (GIL) in CPython, threads 
# are not suitable for achieving true parallelism with CPU-bound tasks.
import threading

def worker():
    print("Worker thread")

def newworker():
    print("New Worker thread")

# Create and start a new thread
thread = threading.Thread(target=newworker)
thread.start()



# Multiprocessing:
# The multiprocessing module provides a way to spawn multiple processes, 
# each running its own Python interpreter. Unlike threads, processes can achieve 
# true parallelism and are suitable for CPU-bound tasks. The module includes tools 
# for process creation, communication, and synchronization.

import multiprocessing

def worker():
    print("Worker process")

# Create and start a new process
process = multiprocessing.Process(target=worker)
process.start()

# Asyncio:
# The asyncio module is a powerful framework for asynchronous programming in Python.
#  It introduces the concept of coroutines, which are special functions that can be
#  paused and resumed while waiting for I/O operations or other coroutines. The 
# module provides an event loop that schedules and manages these coroutines 
# efficiently.
import asyncio

async def worker():
    print("Worker coroutine")

    

# Create and run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(worker())

# Asyncio also offers other features such as asynchronous I/O operations,
#  synchronization primitives like locks and semaphores, and utilities for
#   creating and managing tasks and futures


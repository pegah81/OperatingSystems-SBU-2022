import threading

global production_count, buffer_capacity, buffer, in_index, out_index, empty, mutex, full
production_count = 20
buffer_capacity = 7
buffer = [None]*buffer_capacity
in_index = 0
out_index = 0
mutex = threading.Semaphore(1)
empty = threading.Semaphore(buffer_capacity)
full = threading.Semaphore(0)
produced = 0
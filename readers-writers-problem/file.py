import threading

readers_c = 0
write = threading.Semaphore(1)
mutex = threading.Semaphore(1)


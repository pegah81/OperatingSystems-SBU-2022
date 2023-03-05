import threading
import buffer
import time


class Consumer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        consumed = 0

        while (consumed < buffer.production_count):
            buffer.full.acquire()
            buffer.mutex.acquire()

            data = buffer.buffer[buffer.out_index]
            buffer.buffer[buffer.out_index] = None
            buffer.out_index = (buffer.out_index + 1) % buffer.buffer_capacity
            print(f"consumer {self.name} consumed {data + 1}")
            time.sleep(1)

            buffer.mutex.release()
            buffer.empty.release()
            time.sleep(3)

            consumed += 1

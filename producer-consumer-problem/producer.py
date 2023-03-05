import threading
import buffer
import time

class Producer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        while(buffer.produced < buffer.production_count):
            buffer.empty.acquire()
            buffer.mutex.acquire()

            buffer.buffer[buffer.in_index] = buffer.produced
            buffer.in_index = (buffer.in_index + 1) % buffer.buffer_capacity
            print(f"producer {self.name} produced {buffer.produced + 1}")
            time.sleep(0.5)

            buffer.mutex.release()
            buffer.full.release()
            time.sleep(0.5)

            buffer.produced += 1


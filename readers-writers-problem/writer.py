import threading
import file
import time

class Writer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            file.write.acquire()
            print(f"{self.name} is writing.")
            time.sleep(3)
            file.write.release()
            time.sleep(0.25)
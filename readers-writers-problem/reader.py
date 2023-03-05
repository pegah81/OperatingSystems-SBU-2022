import threading
import file
import time

class Reader(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            file.mutex.acquire()
            file.readers_c+=1
            if(file.readers_c == 1):
                file.write.acquire()
            file.mutex.release()
            print(f"{self.name} is reading.")
            time.sleep(2)
            file.mutex.acquire()
            file.readers_c -= 1
            if (file.readers_c == 0):
                file.write.release()
            file.mutex.release()
            time.sleep(0.25)


import time
import threading
import table

class Philosopher(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num  # philosopher number
        self.left = (num + table.n - 1) % table.n
        self.right = (num + 1) % table.n

    def run(self):
        while True:
            self.think()
            self.take_forks()
            print(f"philosopher {self.num} is eating")
            time.sleep(8)
            self.put_forks()

    def think(self):
        time.sleep(3)

    def take_forks(self):
        table.mutex.acquire()
        table.state[self.num] = 'HUNGRY'
        print(f"philosopher {self.num} is hungry")
        table.test(self.num)
        table.mutex.release()
        table.s[self.num].acquire()

    def put_forks(self):
        table.mutex.acquire()
        table.state[self.num] = 'THINKING'
        print(f"philosopher {self.num} is thinking")
        table.test(self.left)
        table.test(self.right)
        table.mutex.release()
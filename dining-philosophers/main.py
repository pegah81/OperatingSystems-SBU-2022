from philosopher import Philosopher

p0 = Philosopher(0)
p1 = Philosopher(1)
p2 = Philosopher(2)
p3 = Philosopher(3)
p4 = Philosopher(4)

def main():
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()

if __name__ == "__main__":
    main()

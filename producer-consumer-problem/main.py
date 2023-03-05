
from producer import Producer
from consumer import Consumer

producer = Producer("1")
consumer1 = Consumer("1")
consumer2 = Consumer("2")

def main():
    producer.start()
    consumer1.start()
    consumer2.start()

if __name__ == "__main__":
    main()
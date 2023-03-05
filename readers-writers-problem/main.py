import reader
import writer

w1 = writer.Writer("writer 1")
w2 = writer.Writer("writer 2")

r1 = reader.Reader("reader 1")
r2 = reader.Reader("reader 2")
r3 = reader.Reader("reader 3")



def main():
    w1.start()
    w2.start()
    r1.start()
    r2.start()
    r3.start()

if __name__ == "__main__":
    main()
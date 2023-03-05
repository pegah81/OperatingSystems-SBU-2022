import threading
n = 5
mutex = threading.Semaphore(1)
state = []
s = []
p = []
[s.append(threading.Semaphore(0)) for i in range(n)]
[state.append("THINKING") for i in range(n)]

def test(i):
    left = (i + n - 1) % n
    right = (i + 1) % n
    if (state[i]=='HUNGRY' and state[left]!='EATING' and state[right]!='EATING'):
        state[i]='EATING'
        s[i].release()
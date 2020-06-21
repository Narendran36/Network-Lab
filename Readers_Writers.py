import threading as thread
import random

global x
x = 0
lock = thread.Lock()

def Reader():
    global x
    print('Reader is Reading!')
    lock.acquire()
    print('Shared Data: ', x)
    lock.release()
    print()

def Writer():
    global x
    print('Writer is Writing!')
    lock.acquire()
    x += 1
    print('Writer is Releasing the lock!')
    lock.release()
    print()

if __name__ == '__main__':
    for i in range(0,10):
        randomNumber = random.randint(0, 100)
        if (randomNumber > 50):
            Thread1 = thread.Thread(target = Reader)
            Thread1.start()
        else:
            Thread2 = thread.Thread(target = Writer)
            Thread2.start()
Thread1.join()
Thread2.join()

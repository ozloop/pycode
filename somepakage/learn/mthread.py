import threading
import sys
import time

def showa():
    while True:
        lockb.acquire()   #获取对方的锁，释放自己的锁
        print('a',end='')
        sys.stdout.flush()   #释放缓冲区
        time.sleep(0.1)
        locka.release()

def showb():
    while True:
        locka.acquire()
        print('b',end='')
        sys.stdout.flush() 
        time.sleep(0.1)
        lockb.release()
        
if __name__=='__main__':
    locka=threading.Lock()  #定义3个互斥锁
    lockb=threading.Lock()
 
    t1=threading.Thread(target=showa)   #定义3个线程
    t2=threading.Thread(target=showb)
 
    locka.acquire()   #先锁住a,b锁，保证先打印a
 
    t1.start()
    t2.start()
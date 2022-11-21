import time


def scheduler(f,n):

    while(1):
        f()
        time.sleep(n/1000)
    



def hello():
    print("hello")

scheduler(hello, 1)
from multiprocessing.connection import wait
from time import sleep


N=int(input("N? "))

def countdown(N):
    print(N)
    sleep(1)
    N=N-1
    if N>0:
     countdown(N)


countdown(N)
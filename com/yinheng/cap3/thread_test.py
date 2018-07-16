import time
import threading

def print_time():
    while True:
        time.sleep(1)
        print(get_time())


def get_time():
    return time.localtime(time.time())



threading.Thread(target=print_time(), name = "T1").start()
threading.Thread(target=print("Hello"), name = "T2").start()

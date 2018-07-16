import time
import threading

def get_time():
    while True:
        print(time.localtime(time.time()))
        time.sleep(1)

threading.Thread(target = get_time).start()
print("hello")
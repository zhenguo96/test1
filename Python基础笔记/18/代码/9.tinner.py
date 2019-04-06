import threading
import time

def sing():
    print("啦啦啦")

if __name__ == "__main__":
    p = threading.Timer(3,sing)
    p.start()

















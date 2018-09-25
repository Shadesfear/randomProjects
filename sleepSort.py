import time
import threading

items = [2,4,5,2,10,1]

class myThread (threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        sleepSort(self.counter)


def sleepSort(x):
    time.sleep(x)
    print(x)


for index, line in enumerate(items):
    thread = myThread(line)
    thread.start()

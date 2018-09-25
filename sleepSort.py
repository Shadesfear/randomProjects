import time
import threading

items = [2,4,5,2,10,1]
threads = []

class myThread (threading.Thread):

    def __init__(self, line):
        threading.Thread.__init__(self)
        self.line = line

    def run(self):
        sleepSort(self.line)


def sleepSort(x):
    time.sleep(x)
    print(x)


for index, line in enumerate(items):
    thread = myThread(line)
    threads.append(thread)

for thread in threads:
    thread.start()

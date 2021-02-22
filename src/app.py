import json
from DataStructures import Queue
from sms import send

queue = Queue(mode="FIFO")

def print_queue():
    print("Printing the entire list...")
    print(queue.get.queue())


def add(name):
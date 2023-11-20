from os import system
from threading import Thread


def clear_terminal():
    thread = Thread(group=None, target=system, args=("clear",))
    thread.start()

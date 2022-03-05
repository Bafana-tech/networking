import sys
import time

def print_slow(str):
        for char in str:
            time.sleep(.1)
            sys.stdout.write(char)
            sys.stdout.flush()

print_slow('Hello')
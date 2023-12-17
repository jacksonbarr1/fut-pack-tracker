import os
import time


def wait_for_initializer():
    while not os.path.exists('tmp/initializer_complete'):
        print("Waiting for db-initializer...")
        time.sleep(5)

if __name__ == '__main__':
    wait_for_initializer()
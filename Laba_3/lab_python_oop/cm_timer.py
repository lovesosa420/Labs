import time
from contextlib import contextmanager
from time import sleep


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time:', time.time() - self.start_time)


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    print('time:', time.time() - start_time)


if __name__ == '__main__':
    with cm_timer_1():
        sleep(1.5)

    with cm_timer_2():
        sleep(1.0)

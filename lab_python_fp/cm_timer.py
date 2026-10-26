from contextlib import contextmanager
from time import perf_counter, sleep


class cm_timer_1:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, error_type, error, traceback):
        print(f"time: {perf_counter() - self.start:.4f}")
        return False


@contextmanager
def cm_timer_2():
    start = perf_counter()
    try:
        yield
    finally:
        print(f"time: {perf_counter() - start:.4f}")


if __name__ == "__main__":
    print("Таймер на основе класса:")
    with cm_timer_1():
        sleep(0.1)

    print("Таймер на основе contextlib:")
    with cm_timer_2():
        sleep(0.1)

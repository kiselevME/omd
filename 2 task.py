import sys
from datetime import datetime
from typing import Callable


def timed_output(function: Callable):
    def wrapper(*args, **kwargs):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sys.stdout.write(f'[{current_time}] ')
        return function(*args, **kwargs)

    return wrapper


@timed_output
def print_greeting(name: str):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")

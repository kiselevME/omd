import sys
from typing import Callable


def redirect_output(filepath: str):
    def decorator(function: Callable):
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            sys.stdout = open(filepath, 'w')
            res = function(*args, **kwargs)
            sys.stdout.close()
            sys.stdout = original_stdout
            return res

        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()

    print('Обычный print снова выводит результат в консоль')
    print('Открываем файл для чтения:')
    with open('./function_output.txt', 'r') as f:
        for line in f:
            print(line, end='')

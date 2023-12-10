import sys
from datetime import datetime

# запоминаем оригинальный метод write
original_write = sys.stdout.write


def my_write(string_text: str) -> int:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res = original_write(f'[{current_time}] {string_text}')
    # подменяем write на оригинальный
    sys.stdout.write = original_write
    return res


if __name__ == '__main__':
    # подменяем write на собственную реализацию
    sys.stdout.write = my_write
    print('1, 2, 3')

    print('После этого шага print работает как обычно')

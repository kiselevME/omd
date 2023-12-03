class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):

        return f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}'\
            '{self.MOD}'

    def __eq__(self, value) -> bool:
        if isinstance(value, Color):
            return self.r == value.r and self.g == value.g and\
                  self.b == value.b
        else:
            return False


if __name__ == '__main__':
    red = Color(255, 1, 0)
    green = Color(0, 255, 0)
    red_2 = Color(255, 1, 0)
    print(red == green)
    print(red == red_2)
    print(red == 1)

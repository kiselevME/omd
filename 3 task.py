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
            f'{self.MOD}'

    def __eq__(self, other) -> bool:
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and\
                  self.b == other.b
        else:
            return False

    def __add__(self, other):
        return Color(min(self.r + other.r, 255),
                     min(self.g + other.g, 255),
                     min(self.b + other.b, 255))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)

    print(red + green)

class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):

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

    def __hash__(self) -> int:
        return int(self.r + 1e3 * self.g + 1e6 * self.b)


if __name__ == '__main__':
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

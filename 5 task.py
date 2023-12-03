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
        return hash((self.r, self.g, self.b))

    def __mul__(self, c: float):
        if (c >= 0) and (c <= 1):
            cl = -256 * (1 - c)
            F = (259 * (cl + 255)) / (255 * (259 - cl))

            r = int(F * (self.r - 128) + 128)
            g = int(F * (self.g - 128) + 128)
            b = int(F * (self.b - 128) + 128)
            return Color(r, g, b)
        else:
            raise ValueError

    def __rmul__(self, c: float):
        return self * c


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
    print(0.5 * red)

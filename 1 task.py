class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'

        return f'{START};{self.r};{self.g};{self.b}{MOD}●{END}{MOD}'


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print('red:', red)

    green = Color(0, 255, 0)
    print('green:', green)

    blue = Color(0, 0, 255)
    print('blue:', blue)

    white = Color(255, 255, 255)
    print('white:', white)

    black = Color(0, 0, 0)
    print('black:', black)

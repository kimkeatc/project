import math


def print_diamond(size: int) -> None:
    
    unicode_character_black_diamond = "*"
    for row in range(-size, size + 1):
        text = ""
        for column in range(-size, size + 1):
            distance = math.sqrt((row ** 2) * (column ** 2))
            text += " " if distance >= size else "*"
        print(text)


if __name__ == "__main__":
    size = 0
    print(f"Generate diamond with size of {size}")
    print_diamond(size)
    size = 1
    print(f"Generate diamond with size of {size}")
    print_diamond(size)
    size = 2
    print(f"Generate diamond with size of {size}")
    print_diamond(size)
    size = 3
    print(f"Generate diamond with size of {size}")
    print_diamond(size)

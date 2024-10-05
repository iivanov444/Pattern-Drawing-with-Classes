from .pattern import pattern_class
import random

class square_with_hollow_center_pattern(pattern_class):
    def __init__(self, pattern_type, subpattern_type, size):
        super().__init__(pattern_type, subpattern_type, size)

    def small_letters_increasing_order(self):
        character = 97  # 'a'
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size-1 or j == 0 or j == self.size-1:
                    print(chr(character), end="")
                    if character >= 122:
                        character = 97
                    else:
                        character += 1
                else:
                    print(" ", end="")
            print()

    def small_letters_decreasing_order(self):
        character = 122  # 'z'
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    print(chr(character), end="")
                    if character <= 97:
                        character = 122
                    else:
                        character -= 1
                else:
                    print(" ", end="")
            print()

    def small_letters_randomized_order(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    random_int = random.randint(ord('a'), ord('z'))
                    print(chr(random_int), end="")
                else:
                    print(" ", end="")
            print()

    def capital_letters_increasing_order(self):
        character = 65  # 'A'
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    print(chr(character), end="")
                    if character >= 90:
                        character = 65
                    else:
                        character += 1
                else:
                    print(" ", end="")
            print()

    def capital_letters_decreasing_order(self):
        character = 90  # 'Z'
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    print(chr(character), end="")
                    if character <= 65:
                        character = 90
                    else:
                        character -= 1
                else:
                    print(" ", end="")
            print()

    def capital_letters_randomized_order(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    random_int = random.randint(ord('A'), ord('Z'))
                    print(chr(random_int), end="")
                else:
                    print(" ", end="")
            print()

    def numbers_increasing_order(self):
        start = 1
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    character = str(start)
                    print(character, end="")
                    if start >= 9:
                        start = 1
                    else:
                        start += 1
                else:
                    print(" ", end="")
            print()

    def numbers_decreasing_order(self):
        start = 9
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    character = str(start)
                    print(character, end="")
                    if start <= 1:
                        start = 9
                    else:
                        start -= 1
                else:
                    print(" ", end="")
            print()

    def numbers_randomized_order(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    random_int = random.randint(1, 9)
                    character = str(random_int)
                    print(character, end="")
                else:
                    print(" ", end="")
            print()

    def specific_characters(self):
        while True:
            character = input("Enter a character: ")[0]
            if character:
                break

        print()
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if i == 1 or i == self.size or j == 1 or j == self.size:
                    print(character, end="")
                else:
                    print(" ", end="")
            print()

    def randomized_characters(self):
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if i == 1 or i == self.size or j == 1 or j == self.size:
                    random_int = random.randint(33, 126)
                    random_character = chr(random_int)
                    print(random_character, end="")
                else:
                    print(" ", end="")
            print()

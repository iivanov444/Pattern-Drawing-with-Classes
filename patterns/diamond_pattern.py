from .pattern import pattern_class
import random

class diamond_class(pattern_class):
    def __init__(self, pattern_type, subpattern_type, size):
        super().__init__(pattern_type, subpattern_type, size)

    def small_letters_increasing_order(self):
        character = 97  # 'a'
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(chr(character), end="")
                character += 1
                if character > 122:
                    character = 97
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                print(chr(character), end="")
                character += 1
                if character > 122:
                    character = 97
            print()

    def small_letters_decreasing_order(self):
        character = 122  # 'z'
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(chr(character), end="")
                character -= 1
                if character < 97:
                    character = 122
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                print(chr(character), end="")
                character -= 1
                if character < 97:
                    character = 122
            print()

    def small_letters_randomized_order(self):
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                character = random.randint(ord('a'), ord('z'))
                print(chr(character), end="")
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                character = random.randint(ord('a'), ord('z'))
                print(chr(character), end="")
            print()

    def capital_letters_increasing_order(self):
        character = 65  # 'A'
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(chr(character), end="")
                character += 1
                if character > 90:
                    character = 65
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                print(chr(character), end="")
                character += 1
                if character > 90:
                    character = 65
            print()

    def capital_letters_decreasing_order(self):
        character = 90  # 'Z'
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(chr(character), end="")
                character -= 1
                if character < 65:
                    character = 90
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                print(chr(character), end="")
                character -= 1
                if character < 65:
                    character = 90
            print()

    def capital_letters_randomized_order(self):
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                character = random.randint(ord('A'), ord('Z'))
                print(chr(character), end="")
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                character = random.randint(ord('A'), ord('Z'))
                print(chr(character), end="")
            print()

    def numbers_increasing_order(self):
        start = 1
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                character = str(start)
                print(character, end="")
                start += 1
                if start > 9:
                    start = 1
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                character = str(start)
                print(character, end="")
                start += 1
                if start > 9:
                    start = 1
            print()

    def numbers_decreasing_order(self):
        start = 9
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                character = str(start)
                print(character, end="")
                start -= 1
                if start < 1:
                    start = 9
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                character = str(start)
                print(character, end="")
                start -= 1
                if start < 1:
                    start = 9
            print()

    def numbers_randomized_order(self):
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                random_int = random.randint(1, 9)
                character = str(random_int)
                print(character, end="")
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                random_int = random.randint(1, 9)
                character = str(random_int)
                print(character, end="")
            print()

    def specific_characters(self):
        while True:
            character = input("Enter a character: ")[0]
            if character:
                break
        print()
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(character, end="")
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                print(character, end="")
            print()

    def randomized_characters(self):
        for a1 in range(1, (self.size + 1) // 2 + 1):
            for a2 in range((self.size + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                random_int = random.randint(33, 126)
                character = chr(random_int)
                print(character, end="")
            print()

        for a1 in range((self.size + 1) // 2 + 1, self.size + 1):
            for a2 in range(a1 - (self.size + 1) // 2):
                print(" ", end="")
            for a3 in range((self.size + 1 - a1) * 2 - 1):
                random_int = random.randint(33, 126)
                character = chr(random_int)
                print(character, end="")
            print()

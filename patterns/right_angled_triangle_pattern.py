from .pattern import pattern_class
import random

class right_angled_triangle_class(pattern_class):
    def __init__(self, pattern_type, subpattern_type, size):
        super().__init__(pattern_type, subpattern_type, size)

    def small_letters_increasing_order(self):
        rows_list = []
        character = 97  # 'a'
        for _ in range(self.size):
            rows_list.append(chr(character))
            character += 1

            if character > 122:
                character = 97

            line = ''.join(rows_list)
            print(line)

    def small_letters_decreasing_order(self):
        rows_list = []
        character = 122 # 'z'
        for _ in range(self.size):
            rows_list.append(chr(character))
            character -= 1

            if character < 97:
                character = 122

            line = ''.join(rows_list)
            print(line)

    def small_letters_randomized_order(self):
        counter = 1
        for _ in range(self.size):
            rows_list = []
            for _ in range(counter):
                random_int = random.randint(ord('a'), ord('z'))
                rows_list.append(chr(random_int))
            counter += 1
            line = ''.join(rows_list)
            print(line)

    def capital_letters_increasing_order(self):
        rows_list = []
        character = 65  # 'A'
        for _ in range(self.size):
            rows_list.append(chr(character))
            character += 1

            if character > 90:
                character = 65

            line = ''.join(rows_list)
            print(line)

    def capital_letters_decreasing_order(self):
        rows_list = []
        character = 65 # 65 = 'A'
        for _ in range(self.size):
            rows_list.append(chr(character))
            character -= 1

            if character > 90:
                character = 65

            line = ''.join(rows_list)
            print(line)

    def capital_letters_randomized_order(self):
        counter = 1
        for _ in range(self.size):
            rows_list = []
            for _ in range(counter):
                random_int = random.randint(ord('A'), ord('Z'))
                rows_list.append(chr(random_int))
            counter += 1
            line = ''.join(rows_list)
            print(line)

    def numbers_increasing_order(self):
        start = 1
        rows_list = []
        for _ in range(self.size):
            character = str(start)
            rows_list.append(character)
            start += 1
            if start > 9:
                start = 1
            line = ''.join(rows_list)
            print(line)

    def numbers_decreasing_order(self):
        start = 9
        rows_list = []
        for _ in range(self.size):
            character = str(start)
            rows_list.append(character)
            start -= 1
            if start < 1:
                start = 9
            line = ''.join(rows_list)
            print(line)

    def numbers_randomized_order(self):
        counter = 1
        for _ in range(self.size):
            rows_list = []
            for _ in range(counter):
                random_int = random.randint(1, 9)
                random_character = str(random_int)
                rows_list.append(random_character)
            counter += 1
            line = ''.join(rows_list)
            print(line)

    def specific_characters(self):
        while True:
            character = input("Enter a character: ")[0]
            if character:
                break
        print()

        rows_list = []
        for _ in range(self.size):
            rows_list.append(character)
            line = ''.join(rows_list)
            print(line)

    def randomized_characters(self):
        counter = 1
        rows_list = []

        for _ in range(self.size, 0, -1):
            rows_list.clear()
            for _ in range(counter):
                random_int = random.randint(33, 126)
                random_character = chr(random_int)
                rows_list.append(random_character)
            counter += 1
            line = ''.join(rows_list)
            print(line)

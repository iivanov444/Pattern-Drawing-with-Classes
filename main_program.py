from patterns import right_angled_triangle_pattern
from patterns import left_angled_triangle_pattern
from patterns import square_with_hollow_center_pattern
from patterns import diamond_pattern
from patterns import pyramid_pattern
from patterns import inverted_pyramid_pattern

def pattern_type_list() -> list:
    def subpattern_type() -> str:
        subpattern_type_dict = {
            1: "Increasing order",
            2: "Decreasing order",
            3: "Randomized order"
            }
        
        print("Subpattern type list:")
        for key, value in subpattern_type_dict.items():
            print(f"{key}. {value}")
            
        while True:
            subpattern_type_input_str = input("Choose subpattern type or exit with <SPACE> key: ")
            if not subpattern_type_input_str:
                main()
            else:
                subpattern_type_input = int(subpattern_type_input_str)
                if subpattern_type_input in range(1, 4):
                    return subpattern_type_dict[subpattern_type_input]
                else:
                    print("Invalid input.")
    
    pattern_type_dict = {
        1: ["Small letters", subpattern_type],
        2: ["Capital letters", subpattern_type],
        3: ["Numbers", subpattern_type],
        4: ["Specific characters", None],
        5: ["Randomized characters", None]
        }

    print("Pattern type list:")
    for key, value in pattern_type_dict.items():
        print(f"{key}. {value[0]}")
    
    while True:
        pattern_type_input_str = input("Choose pattern type or exit with <SPACE> key: ")
        if not pattern_type_input_str:
            main()
        else:
            pattern_type_input = int(pattern_type_input_str)
            if pattern_type_input in range(1, 6):
                _pattern_type = pattern_type_dict[pattern_type_input][0]
                if pattern_type_dict[pattern_type_input][1] != None:
                    _subpattern_type = pattern_type_dict[pattern_type_input][1]()
                else:
                    _subpattern_type = None

                while True:
                    _size = input("Enter size from 3 to 50 or exit with <SPACE> key: ")
                    if not _size:
                        main()
                    else:
                        _size_int = int(_size)
                        if _size_int in range(3, 51, 1):
                            break


                pattern_subpattern_size = [_pattern_type, _subpattern_type, _size_int]
                break
                
            else:
                print("Invalid input.")

    return pattern_subpattern_size

pattern_dict = {
         1: ['Right-angled triangle', right_angled_triangle_pattern.right_angled_triangle_class],
         2: ['Left-angled triangle', left_angled_triangle_pattern.left_angled_triangle_class],
         3: ['Square with hollow center', square_with_hollow_center_pattern.square_with_hollow_center_pattern],
         4: ['Diamond', diamond_pattern.diamond_class],
         5: ['Pyramid', pyramid_pattern.pyramid_class],
         6: ['Inverted Pyramid', inverted_pyramid_pattern.inverted_pyramid_class]
    }

def main():
    while True:
        print("\nPattern list:")
        for key, value in pattern_dict.items():
            print(f"{key}. {value[0]}")

        user_input = input("Choose pattern or exit program with <ENTER> key: ")
        if not user_input:
            raise SystemExit()
        else:
            try:
                user_input = int(user_input)
                if user_input in range(1, 7):
                    pattern_str, pattern_class = pattern_dict[user_input]

                    pattern_subpattern_size = pattern_type_list()
                    pattern_type, subpattern_type, size \
                        = pattern_subpattern_size[0], pattern_subpattern_size[1], pattern_subpattern_size[2]

                    pattern_instance = pattern_class(pattern_type, subpattern_type, size)

                    pattern_type = pattern_instance.get_pattern_type()
                    subpattern_type = pattern_instance.get_subpattern_type()
                    subpattern_str = str(subpattern_type)
                    pattern_subpattern = pattern_type + " + " + subpattern_str

                    pattern_caller_dict = {
                        "Small letters + Increasing order": pattern_instance.small_letters_increasing_order,
                        "Small letters + Decreasing order": pattern_instance.small_letters_decreasing_order,
                        "Small letters + Randomized order": pattern_instance.small_letters_randomized_order,

                        "Capital letters + Increasing order": pattern_instance.capital_letters_increasing_order,
                        "Capital letters + Decreasing order": pattern_instance.capital_letters_decreasing_order,
                        "Capital letters + Randomized order": pattern_instance.capital_letters_randomized_order,

                        "Numbers + Increasing order": pattern_instance.numbers_increasing_order,
                        "Numbers + Decreasing order": pattern_instance.numbers_decreasing_order,
                        "Numbers + Randomized order": pattern_instance.numbers_randomized_order,

                        "Specific characters + None": pattern_instance.specific_characters,

                        "Randomized characters + None": pattern_instance.randomized_characters
                    }

                    print()
                    pattern_caller_dict[pattern_subpattern]()
                else:
                    print("Invalid input. Pattern not found.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")


if __name__ == '__main__':
    main()

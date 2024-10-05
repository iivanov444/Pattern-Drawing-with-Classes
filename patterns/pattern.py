class pattern_class():
    def __init__(self, pattern_type, subpattern_type, size):
        self.pattern_type = pattern_type
        self.subpattern_type = subpattern_type
        self.size = size

    def get_pattern_type(self) -> str:
        return self.pattern_type

    def get_subpattern_type(self) -> str:
        return self.subpattern_type

    def get_size(self) -> int:
        return self.size

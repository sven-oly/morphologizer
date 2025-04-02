# Base class for morphologizer

class morphy_base():
    def __init__(self):
        self.lang_name = 'unknown'
        self.lang_code = 'und'
        self.grammar = None
        sself.fsts = None

    def generate(self):
        return None

    def parse(self):
        return None

    def paradigm(self):
        return None

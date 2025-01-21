# Start of a package that implements morphology in general
# -*- coding: utf-8 -*-


from langmodel import LangModel, Verb

class Morphologizer():
    def __init__(self, model=None):
        # TODO: Define some constants for tense, aspect, person, mood, etc.
        self.lang_codes = ['fr', 'har', 'de', 'eu', 'ff']  # A few suggestions
        self.model = model

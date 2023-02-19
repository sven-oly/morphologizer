# Start of a package that implements morphology in general
# -*- coding: utf-81 -*-

class Morphologizer:
    def __init__(self):
        # TODO: Define some constants for tense, aspect, person, mood, etc.
        self.lang_codes = ['fr', 'de', 'eu', 'ff']  # A few suggestions
        return


class LangInfo:
    def __init__(self, lang_code, script_code='latn'):
        self.lang_code = lang_code
        self.script_code = script_code
        self.moods = []
        self.time_aspect = []
        self.person = []
        self.number = []
        self.classes = []
        self.auxiliary = []

    def verbInfo(self):
        # Things that verbs do
        self.moods = []
        self.time_aspect = []
        self.person = []
        self.number = []
        self.classes = []
        self.auxiliary = []

        # Sets of regular and irregular?
        # which need agreement with nouns?
        # what auxiliary verbs are used?

    def nounInfo(self):
        return

    def pronounInfo(self):
        return

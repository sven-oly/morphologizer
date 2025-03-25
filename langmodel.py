#
# -*- coding: utf-8 -*-

class LangModel:
    def __init__(self, lang_code, script_code='latn'):
        self.lang_code = lang_code
        self.script_code = script_code
        self.lang_name = 'not set'
        self.moods = []
        self.time_aspect = []
        self.person = []
        self.number = []
        self.classes = []
        self.auxiliary = []
        self.noun_classes = []

    def verb(self):
        # Things that verbs do
        return

        # Sets of regular and irregular?
        # which need agreement with nouns?
        # what auxiliary verbs are used?

    def nounInfo(self):
        return

    def pronounInfo(self):
        return


class Verb:
    def __init__(self, lang_info):
        self.lang_info = lang_info
        self.model = lang_info


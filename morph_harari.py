#
# -*- coding: utf-8 -*-

from morphologizer import LangModel, Morphologizer, Verb

# https://en.wikipedia.org/wiki/Harari_language#Verbs

class

class MorphHarari(Morphologizer):
    def __init__(self, model):
        super().__init__(model)
        self.LangModel = HarariLang()
        self.verb = HarariVerb()


class HarariLang(LangModel):
    def __init__(self):
        super().__init__('har')
        self.lang_code = 'har'
        self.script_code = 'Geez'
        self.gender = ['m', 'f']
        self.numbers = ['singular', 'plural']

        
class HarariVerb(Verb):
    def __init__(self, model, infinitive):
        super().__init__(model)

        # Lots to fill in here
        return

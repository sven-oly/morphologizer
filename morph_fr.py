#
# -*- coding: utf-8 -*-

from morphologizer import LangModel, Morphologizer, Verb


class MorphFr(Morphologizer):
    def __init__(self):
        super.__init__(MorphFr, self)
        self.LangModel = FrenchLang()


class FrenchLang(LangModel):
    def __init__(self):
        super.__init__(FrenchLang, LangModel)
        self.lang_code = 'fr'
        self.script_code = 'latn'
        self.gender = ['m', 'f']
        self.numbers = ['singulier', 'pluriel']

        self.subject_pronouns = {
          'singulier': ['je', 'tu', ['il', 'elle', 'on']],
          'pluriel': ['nous', 'vous', ['ils', 'elles']]
        }
        self.pronomia_pronouns = {
          'singulier': ['me', 'te', 'se'],
          'pluriel': ['nous', 'vous', 'se']
        }

        # These special auxiliaries
        self.etre = etre
        self.avoir = avoir

    def verbInfo(self):
        self.classes = ['er', 'ir', 'irregular']
        self.moods = ['indicative', 'subjunctive', 'imperative', 'infinitive', 'participe']
        self.auxiliary = ['etre', 'avoir']

    def auxEtre(self):
        # The verbs that use être as the auxiliary. general verbs of motion
        self.use_etre = ['aller', 'venir']  # Many more...

    def nounInfo(self):
        # Gender affects adjectives and pronouns, and agreement
        # with some verb forms, e.g., participe.
        return


class FrenchVerb(Verb):  # Instance?
    def __init__(self, infinitive, conjugation=None, exceptions=None):
        super.__init__(FrenchVerb, self)

        self.model = FrenchLang()

        # -er, -ir, -re
        # TODO: Normalize the input with diacritis
        self.stem = infinitive[:-2]
        self.ending = infinitive[-2:]  # "er", "ir", "re", etc.
        if infinitive[-3:1] == 'ï':
            self.stem = 'ir'
            self.ending = 'ï'
        else:
            self.stem = infinitive[:-2]
            self.ending = infinitive[-2:]  # "er", "ir", "re", etc.

        if conjugation:
            self.conjugation = conjugation  # Special conjugation provided
            self.irregular = True
        else:
            self.conjugation = None  # Follows regular rules
            self.irregular = False

        self.is_auxiliary = False  # Needed?
        self.persons = [1, 2, 3]

        if exceptions:
            # Add specific cases for number, person, tense, mode,
            self.update_exceptions(exceptions)
            self.irregular = True

        # For agreement of forms with subject
        self.passive_agreement = True  # At least for etre

        self.numbers = ['singulier', 'pluriel']
        self.tenses = ['present', 'passé composé',
                       'imparfait', 'plus-que-parfait',
                       'passé simple', 'passé antérieur',
                       'futur simple', 'futur antérieur',
                       'conditional présent', 'conditional passé']

        self.simple_tenses = ['present',
                              'imparfait',
                              'passé simple',
                              'futur simple',
                              'conditional présent']
        self.modes = ['indicatif', 'subjonctif', 'impératif', 'infinitif', 'participe']

        if infinitive in self.model.use_etre:
            self.auxiliary = self.model.etre
        else:
            self.auxiliary = self.model.avoir  # Default

        self.regular = True  # default

    def combine(self, person, number, verb_form):
        # Returns modified pronoun and verb if contraction is needed
        # 2nd is True or False indicating if modified
        if person == 1 and number == 'singulier':
            # Check if first letter of verb is a vowel. Then use "j'"
            if verb_form[0] in ['a', 'e', 'i', 'o', 'u', 'h']:
                joined = True
                return "j'" + verb_form, joined
        else:
            return verb_form, False

    def update_exceptions(self, exceptions):
        # TODO: update the conjugations with these exceptions
        return

    def conjugate(self, person, number, tense, mode, passive=False):
        # TODO: Add passive voice
        # For regular verbs
        if self.conjugation:
            return self.lookup_conjugation(person, number, tense, mode)
        else:
            if self.ending == 'er':
                return self.conjugate_er(self, person, number, mode)
            elif self.ending == 'ir':
                return self.conjugate_ir(self, person, number, mode)

    def lookup_conjugation(self, person, number, tense, mode):
        if not self.conjugation:
            return None  # Should thrown exception

        values = self.conjugation[mode][tense]
        index = self.get_person_number_index(person, number)
        return values[index]

    def get_person_number_index(self, person, number):
        # The index of a value where there are 6 items
        if number == 'singuiler':
            return person
        else:
            return person + 3

    def conjugate_er(self, person, number, tense, mode):
        endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']

        if mode == 'indicatif':
            if tense == 'présent':
                endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
            elif tense == 'imparfait':
                endings = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
            elif tense == 'passé simple':
                endings = ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent']
            elif tense == 'futur':
                endings = ['erai', 'eras', 'era', 'erons', 'erez', 'eront']
            elif tense == 'conditionel présent':
                endings = ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']
        elif mode == 'subjontif':
            if tense == 'présent':
                endings = ['esse', 'esses', 'esse', 'issions', 'issiez', 'issent']
            elif tense == 'imparfait':
                endings = ['esse', 'esses', 't', 'issions', 'issiez', 'issent']

        if tense in self.simple_tenses:
            ending_index = self.get_person_number_index(person, number)
            return self.stem + endings[ending_index]
        else:
            return '%s %s' % (
                self.auxiliary.conjugate(person, number, tense, mode),
                self.conjugate(person, number, 'passé', 'indicatif'))

    def get_auxiliary(self, person, number, tense, mode):
        if self.auxiliary == 'avoir':
            return self.model.avoir.conjugate(person, number, tense, mode)
        else:
            return self.model.etre.conjugate(person, number, tense, mode)

    def conjugate_ir(self, person, number, tense, mode):  # if self.ending == 'ir':
        endings = ['is', 'is', 'it', 'issons', 'issez', 'issent']
        if tense == 'présent':
            endings = ['is', 'is', 'it', 'issons', 'issez', 'issent']
        elif tense == 'imparfait':
            endings = ['issais', 'issais', 'issait', 'issions', 'issiez', 'issaient']
        elif tense == 'passé simple':
            endings = ['is', 'is', 'it', 'îmes', 'ites', 'irent']
        elif tense == 'futur':
            endings = ['irais', 'iras', 'ira', 'irons', 'irez', 'iront']
        elif tense == 'conditionel présent':
            endings = ['irais', 'iras', 'ira', 'irions', 'iriez', 'iraient']
        if tense in self.simple_tenses:
            ending_index = self.get_person_number_index(person, number)
            return self.stem + endings[ending_index]
        else:
            return '%s %s' % (
               self.auxiliary.conjugate(person, number, tense, mode),
               self.conjugate(person, number, 'passé', 'indicatif'))

    def print_conjugation_table(self):
        # For each mode
        #   For each tense
        # For each number and person
        for mode in self.modes:
            print('  Mode:: %s' % mode)
            for tense in self.tenses:
                print('  Tense: %s' % tense)
                for person in self.persons:
                    # Accumulate the line
                    line = []
                    for number in self.numbers:
                        line.append(self.conjugate(number, person, tense, mode))
                        # This may not work for all lines
                    print('    %20s      %20s' % (line[0], line[1]))


class SpecialCase(FrenchVerb):
    def __init__(self, infinitive, conjugation=None):
        self.infinitive = infinitive
        self.irregular = True
        self.auxiliary = 'avoir'  # for most
        self.conjugation = conjugation


# Info about specific verbs
etre_conjugation = {
  'indicative': {
    # Each list, 3 singulier forms, then the pluriel forms
    # For each composed form, add 'eu'
    'présent': ['suis', 'es', 'est', 'somme', 'etes', 'sont'],
    'passé composé': ['ai  v', 'as été', 'a été',
                        'avons été', 'avez été', 'ont été'],
    'imparfait': ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
    'plus-que-parfait': ['avais été', 'avais été', 'avait été',
                         'avions été', 'aviez été', 'avaient été'],  # Add 'eu' to imparfait
    'passé simple': ['fus', 'fus', 'fut', 'fûmes', 'fûtes', 'furent'],
    'passé antérieur': ['eus été', 'eus été', 'eut été',
                          'eûmes été', 'eûtes été', 'eurent été'],
    'futur': ['serai', 'seras', 'sera', 'serons', 'surez', 'seront'],
    'futur antérieur': ['aurai été', 'auras été', 'aura été',
                         'aurons été', 'aurez été', 'auront été'],
    'conditional présent': ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient'],
    'conditional passé': ['aurais été', 'aurais été', 'aurait été',
                           'aurions été', 'auriez été', 'auraient été'],
    # Plus the composed forms
  },
  'subjontif': {
    'présent': ['sois', 'sois', 'soit', 'soyons', 'soyez', 'soient'],
    'passé': ['aie été', 'aies été', 'ait été',
               'ayons été', 'ayes été', 'aient été'],
    'imparfait': ['fusse', 'fusses', 'fut', 'fussions', 'fussiez', 'fussent'],
    'plus-que-parfait': ['eusse été', 'eusses été', 'eut été',
                         'eussions été', 'eussiez été', 'eussent été']
  },
  'imperatif': {
    'présent': ['sois', 'soyons', 'soyez'],  # for tu, nous, vous
    'passé': ['aie été', 'ayons été', 'ayez été'],
  },
  'infinitif': {
    'présent': 'avoir',
    'passé': 'avoir été',
  },
  'participe': {
    'présent': 'étant',
    'passé': 'été',
    'passe composé́': 'ayant été'
  },
}
etre = FrenchVerb('être', etre_conjugation)

avoir_conjugation = {
  'indicative': {
    # Each list, 3 singulier forms, then the pluriel forms
    # For each composed form, add 'eu'
    'présent': ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
    'passé composé': ['ai eu', 'as eu', 'a eu',
                        'avons eu', 'avez eu', 'ont eu'],
    'imparfait': ['avais', 'avais', 'avait', 'avion', 'aviez', 'avaient'],
    'plus-que-parfait': [],  # Add 'eu' to imparfait
    'passé simple': ['eus', 'eus', 'eut',
                      'eûmes', 'eûtes', 'eurent'],
    'passé antérieur': ['eus eu', 'eus eu', 'eut eu',
                          'eûmes eu', 'eûtes eu', 'eurent eu'],
    'futur': ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
    'futur antérieur': ['aurai eu', 'auras eu', 'aura eu',
                         'aurons eu', 'aurez eu', 'auront eu'],
    'conditional présent': ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient'],
    'conditional passé': ['aurais eu', 'aurais eu', 'aurait eu',
                           'aurions eu', 'auriez eu', 'auraient eu'],
    # Plus the composed forms
  },
  'subjontif': {
    'présent': ['aie', 'aies', 'ait', 'ayons', 'ayez', 'aient'],
    'passé': ['aie eu', 'aies eu', 'ait eu',
               'ayons eu', 'ayez eu', 'aient eu'],
    'imparfait': ['eusse', 'eusses', 'eut', 'eussions', 'eussiez', 'eussent'],
    'plus-que-parfait': ['eusse eu', 'eusses eu', 'eut eu',
                         'eussions eu', 'eussiez eu', 'eussent eu']
  },
  'imperatif': {
    'présent': ['aie', 'ayons', 'ayez'],  # for tu, nous, vous
    'passé': ['aie eu', 'ayons eu', 'ayez eu'],
  },
  'infinitif': {
    'présent': 'avoir',
    'passé': 'avoir eu',
  },
  'participe': {
    'présent': 'ayant',
    'passé': 'eu',
    'passe composé́': 'ayant eu'
  },
}
avoir = FrenchVerb('avoir', avoir_conjugation)


def main():
    words = ['être', 'avoir', 'aimer', 'finir', 'prendre', 'haïr', 'voir', 'devoir', ]
    morph = MorphFr()
    for word in words:
        v = FrenchVerb(word)
        print('Infinitive: %s, stem: %s' % (v.infinitive, v.stem))
        v.print_conjugation_table()


if __name__ == "__main__":
    main()

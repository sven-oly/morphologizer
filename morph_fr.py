#!/usr/bin/python3
# -*- coding: utf-8 -*-

from morphologizer import Morphologizer
from langmodel import LangModel, Verb


class MorphFr(Morphologizer):
    def __init__(self, model=None):
        #super().__init__(model)
        self.LangModel = FrenchLang()
        self.verbModel = None

        # Example to get started
        self.verbs = []

    def setVerb(self, infinitive):
        self.verbModel = FrenchVerb(self.LangModel, infinitive)

class FrenchLang(LangModel):
    def __init__(self):
        #super().__init__('fr')
        self.lang_code = 'fr'
        self.script_code = 'latn'
        self.gender = ['m', 'f']
        self.numbers = ['singulier', 'pluriel']

        self.subject_pronouns = {
          'singulier': ['je', 'tu', ['il', 'elle', 'on']],
          'pluriel': ['nous', 'vous', ['ils', 'elles']]
        }
        self.pronomial_pronouns = {
          'singulier': ['me', 'te', 'se'],
          'pluriel': ['nous', 'vous', 'se']
        }
        self.verbInfo()
        self.etre = None
        self.avoir = None

        self.auxEtre()
        self.nounInfo()

    def setAuxiliary(self, aux_verb):
        self.aux_verb = aux_verb
        
    def setEtre(self, etre):
        self.etre = etre

    def setAvoir(self, avoir):
        self.avoir = avoir

    def verbInfo(self):
        self.verb_classes = ['er', 'ir', 'irregular']
        self.moods = ['indicative', 'subjunctive', 'imperative', 'infinitive', 'participe']
        self.auxiliary = ['etre', 'avoir']

    def auxEtre(self):
        # The verbs that use être as the auxiliary. general verbs of motion
        self.use_etre = ['aller', 'venir']  # Many more...

    def nounInfo(self):
        # Gender affects adjectives and pronouns, and agreement
        # with some verb forms, e.g., participe.
        self.genders = ['m', 'f']
        return


class FrenchVerb(Verb):  # Instance?
    def __init__(self, model, infinitive,
                 conjugation=None, exceptions=None, use_etre=False):
        #super().__init__(model)

        # -er, -ir, -re
        # TODO: Normalize the input with diacritics
        self.model = model
        self.aux_verb = 'avoir'  # Default
        self.infinitive = infinitive
        self.stem = infinitive[:-2]
        if infinitive == 'avoir':
            self.ending = 'er'
            if self.model.avoir:
                self.conjugation = self.model.avoir.conjugation
            else:
                self.conjugation = conjugation
        if infinitive == 'être':
            self.ending = 're'
            if self.model.etre:
                self.conjugation = self.model.etre.conjugation
            else:
                self.conjugation = conjugation
        else:
            self.ending = infinitive[-2:]


        if infinitive[-3:1] == 'ï':
            self.stem = 'ir'
            self.ending = 'ï'
        else:
            self.stem = infinitive[:-2]
            self.ending = infinitive[-2:]  # "er", "ir", "re", etc.

        self.conjugation = conjugation  # Special conjugation provided
        if conjugation:
            self.irregular = True
        else:
            self.irregular = False

        self.use_etre = use_etre  # The auxiliary
        if infinitive in self.model.use_etre:
          self.auxiliary = self.model.etre
        else:
          self.auxiliary = self.model.avoir  # Default
        self.is_auxiliary = False  # Needed?
        self.persons = [1, 2, 3]

        if exceptions:
            # Add specific cases for number, person, tense, mode,
            self.update_exceptions(exceptions)
            self.irregular = True

        # For agreement of forms with subject
        self.passive_agreement = True  # At least for etre

        self.numbers = ['singulier', 'pluriel']
        self.modes = ['indicatif',
                      'subjonctif',
                      'impératif',
                      'infinitif',

                      'participe']

        self.mode_tenses = {
          'indicatif': ['présent', 'passé composé',
                        'imparfait', 'plus-que-parfait',
                        'passé simple', 'passé antérieur',
                        'futur simple', 'futur antérieur',
                        'conditionnel présent', 'conditionnel passé'
                        ],
          'subjonctif': ['présent', 'passé',
                         'imparfait', 'plus-que-parfait'
                         ],
          'impératif': ['présent', 'passé'],
          'infinitif': ['présent', 'passé'],
          'participe': ['présent', 'passé composé', 'passé']
        }

        self.simple_tenses = ['présent',
                              'imparfait',
                              'passé simple',
                              'futur simple',
                              'conditionnel présent']
        self.simple_to_compound_tenses = {
            'passé composé': 'présent',
            'plus-que-parfait': 'imparfait',
            'passé antérieur': 'passé simple',
            'futur antérieur': 'futur simple',
            'conditionnel passé': 'conditionnel présent',
            'passé': 'présent'}

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
        # For regular verbs
        if self.conjugation:
            return self.lookup_conjugation(person, number, tense, mode)
        else:
            if self.ending == 'er':
                return self.conjugate_er(person, number, tense, mode)
            elif self.ending == 'ir':
                return self.conjugate_ir(person, number, tense, mode)

    def lookup_conjugation(self, person, number, tense, mode):
        if not self.conjugation:
            return None  # Should thrown exception

        if mode in self.conjugation and tense in self.conjugation[mode]:
          values = self.conjugation[mode][tense]
          if mode == 'participe':
            return values
          else:
            index = self.get_person_number_index(person, number)
            return values[index]
        else:
          return None

    def get_person_number_index(self, person, number):
        # The index of a value where there are 6 items
        if number == 'singulier':
            return person - 1
        else:
            return person + 2

    def conjugate_er(self, person, number, tense, mode):
        endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
        if mode == 'participe':
          if self.conjugation and self.conjugation['participe']:
            return self.conjugation['participe'][tense]
          else:
            # Return regular ending
            return u'%s%s' % (self.stem, u'é')
        if tense in self.simple_tenses:
            if mode == 'indicatif':
                if tense == u'présent':
                    endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
                elif tense == 'imparfait':
                    endings = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
                elif tense == u'passé simple':
                    endings = ['ai', 'as', 'a', u'âmes', u'âtes', u'èrent']
                elif tense == 'futur simple':
                    endings = ['erai', 'eras', 'era', 'erons', 'erez', 'eront']
                elif tense == u'conditionnel présent':
                    endings = ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']
            elif mode == 'subjonctif':
                if tense == u'présent':
                    endings = ['esse', 'esses', 'esse', 'issions', 'issiez', 'issent']
                elif tense == 'imparfait':
                    endings = ['esse', 'esses', 't', 'issions', 'issiez', 'issent']

            ending_index = self.get_person_number_index(person, number)
            return self.stem + endings[ending_index]
        else:
            simple_tense = self.simple_to_compound_tenses[tense]
            helper = self.auxiliary.conjugate(person, number, simple_tense, mode)
            return u'%s %s' % (
                helper,
                self.conjugate(person, number, u'passé', u'participe'))

    def get_auxiliary(self, person, number, tense, mode):
        if self.auxiliary == 'avoir':
            return self.model.avoir.conjugate(person, number, tense, mode)
        else:
            return self.model.etre.conjugate(person, number, tense, mode)

    def conjugate_ir(self, person, number, tense, mode):  # if self.ending == 'ir':
        endings = ['is', 'is', 'it', 'issons', 'issez', 'issent']
        if mode == 'participe':
          if self.conjugation and self.conjugation['participe']:
            return self.conjugation['participe'][tense]
          else:
            # Return regular ending
            return self.stem + 'i'
        if tense in self.simple_tenses:
          if mode == u'indicatif':
            # Return regular ending
            if tense == 'présent':
                endings = ['is', 'is', 'it', 'issons', 'issez', 'issent']
            elif tense == 'imparfait':
                endings = ['issais', 'issais', 'issait', 'issions', 'issiez', 'issaient']
            elif tense == u'passé simple':
                endings = ['is', 'is', 'it', 'îmes', 'ites', 'irent']
            elif tense == 'futur simple':
                endings = ['irais', 'iras', 'ira', 'irons', 'irez', 'iront']
            elif tense == 'conditionnel présent':
                endings = ['irais', 'irais', 'irat', 'irions', 'iriez', 'iraient']
            ending_index = self.get_person_number_index(person, number)
            return self.stem + endings[ending_index]
        else:
          simple_tense = self.simple_to_compound_tenses[tense]
          helper = self.auxiliary.conjugate(person, number, simple_tense, mode)
          return '%s %s' % (
            helper,
            self.conjugate(person, number, u'passé', 'participe'))

    def get_conjugation_table(self):
        lines = []
        # For each number and person
        modes = ['indicatif', 'subjonctif']  # Do the others later
        for mode in modes:
            line = u'  Mode:: %s' % mode
            lines.append(line)
            for tense in self.mode_tenses[mode]:
                line = 'u  Tense: %s' % tense
                lines.append(line)
                for person in self.persons:
                    # Accumulate the line
                    line = []
                    for number in self.numbers:
                        result = self.conjugate(person, number, tense, mode)
                        line.append(result)
                        # This may not work for all lines
                    lines.append('    %20s      %20s' % (line[0], line[1]))

        return '\n'.join(lines)
    
    def print_conjugation_table(self):
        # For each mode
        #   For each tense
        # For each number and person
        modes = ['indicatif', 'subjonctif']  # Do the others later
        for mode in modes:
            print('  Mode:: %s' % mode)
            for tense in self.mode_tenses[mode]:
                print('  Tense: %s' % tense)
                for person in self.persons:
                    # Accumulate the line
                    line = []
                    for number in self.numbers:
                        result = self.conjugate(person, number, tense, mode)
                        line.append(result)
                        # This may not work for all lines
                    print('    %20s      %20s' % (line[0], line[1]))


# These special auxiliaries
def setupBasicFrench(theModel):
    etre_conjugation = {
  'indicatif': {
    # Each list, 3 singulier forms, then the pluriel forms
    # For each composed form, add 'eu'
    'présent':
      ['suis', 'es', 'est', 'somme', 'etes', 'sont'],
    u'passé composé':
      ['ai été', 'as été', 'a été',
       ' avons été', 'avez été', 'ont été'],
    'imparfait':
      ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
    'plus-que-parfait':
      ['avais été', 'avais été', 'avait été',
       'avions été', 'aviez été', 'avaient été'],  # Add 'eu' to imparfait
    u'passé simple':
      ['fus', 'fus', 'fut', 'fûmes', 'fûtes', 'furent'],
    u'passé antérieur':
      ['eus été', 'eus été', 'eut été',
       'eûmes été', 'eûtes été', 'eurent été'],
    'futur simple':
      ['serai', 'seras', 'sera', 'serons', 'serez', 'seront'],
    'futur antérieur':
      [u'aurai été', u'auras été', u'aura été',
       u'aurons été', u'aurez été', u'auront été'],
    'conditionnel présent':
      ['serais', 'serais', 'serait', 'serions', 'seriez', 'seraient'],
    u'conditionnel passé':
      [u'aurais été', u'aurais été', u'aurait été',
       u'aurions été', u'auriez été', u'auraient été'],
    # Plus the composed forms
  },
  'subjonctif': {
    'présent':
      ['sois', 'sois', 'soit', 'soyons', 'soyez', 'soient'],
    'passé':
      ['aie été', 'aies été', 'ait été',
       'ayons été', 'ayes été', 'aient été'],
    'imparfait':
      ['fusse', 'fusses', 'fut', 'fussions', 'fussiez', 'fussent'],
    'plus-que-parfait':
      ['eusse été', 'eusses été', 'eut été',
       'eussions été', 'eussiez été', 'eussent été']
  },
  'imperatif': {
    'présent':
      ['sois', 'soyons', 'soyez'],  # for tu, nous, vous
    'passé':
      ['aie été', 'ayons été', 'ayez été'],
  },
  'infinitif': {
    'présent': 'être',
    'passé': 'avoir été',
  },
  'participe': {
    'présent': 'étant',
    'passé': 'été',
    'passe composé́': 'ayant été'
  },
}
    etre = FrenchVerb(theModel, 'être', conjugation=etre_conjugation)

    avoir_conjugation = {
      'indicatif': {
        # Each list, 3 singulier forms, then the pluriel forms
        # For each composed form, add 'eu'
        'présent':
          ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
        'passé composé':
          ['ai eu', 'as eu', 'a eu',
           'avons eu', 'avez eu', 'ont eu'],
        'imparfait':
          ['avais', 'avais', 'avait', 'avions', 'aviez', 'avaient'],
        'plus-que-parfait': [],  # Add 'eu' to imparfait
        'passé simple':
          ['eus', 'eus', 'eut',
           'eûmes', 'eûtes', 'eurent'],
        'passé antérieur':
          ['eus eu', 'eus eu', 'eut eu',
           'eûmes eu', 'eûtes eu', 'eurent eu'],
        'futur simple':
          ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
        'futur antérieur':
          ['aurai eu', 'auras eu', 'aura eu',
           'aurons eu', 'aurez eu', 'auront eu'],
        'conditionnel présent':
          ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient'],
        'conditionnel passé':
          ['aurais eu', 'aurais eu', 'aurait eu',
           'aurions eu', 'auriez eu', 'auraient eu'],
      },
      'subjonctif': {
        'présent':
          ['aie', 'aies', 'ait', 'ayons', 'ayez', 'aient'],
        'passé':
          ['aie eu', 'aies eu', 'ait eu',
           'ayons eu', 'ayez eu', 'aient eu'],
        'imparfait':
          ['eusse', 'eusses', 'eut', 'eussions', 'eussiez', 'eussent'],
        'plus-que-parfait':
          ['eusse eu', 'eusses eu', 'eut eu',
           'eussions eu', 'eussiez eu', 'eussent eu']
      },
      'imperatif': {
        'présent':
          ['aie', 'ayons', 'ayez'],  # for tu, nous, vous
        'passé':
          ['aie eu', 'ayons eu', 'ayez eu'],
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
    avoir = FrenchVerb(theModel, 'avoir', conjugation=avoir_conjugation)

    theModel.setEtre(etre)
    theModel.setAvoir(avoir)

class SpecialCase(FrenchVerb):
    def __init__(self, theModel, infinitive, conjugation=None):
        #super().__init__(infinitive)
        self.infinitive = infinitive
        self.irregular = True
        self.auxiliary = 'avoir'  # for most
        self.conjugation = conjugation


def main():
    words = ['être', 'avoir', 'finir', 'aimer', 'venir', 'prendre',
             'haïr', 'voir', 'devoir', ]
    words = ['prendre']
    frenchLangModel = FrenchLang()
    morph = MorphFr(frenchLangModel)
    setupBasicFrench(frenchLangModel)
    for word in words:
        v = FrenchVerb(frenchLangModel, word)
        print('%s' % '-'*20)
        print('Infinitive: %s, stem: %s' % (v.infinitive, v.stem))
        result = v.get_conjugation_table()
        print(result)

if __name__ == "__main__":
    main()

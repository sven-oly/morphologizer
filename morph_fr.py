#
from morphogizer import morphologizer
from morphogizer import langInfo

class morph_fr(langInfo):
  def __init__(self):
    self.lang_code = 'fr'
    self.script_code = 'latn'

  def verbInfo(self):
    self.classes = ['er', 'ir', 'irregular']
    self.moods = ['indicative', 'subjunctive', 'imperative', 'infinitive', 'participe']
    self.auxiliary = ['etre', 'avoir']


  def nounInfo(self):
    self.gender = ['m', 'f']
    # Gender affects adjectives and pronouns, and agreement
    # with some verb forms, e.g., participe.

class verb():  # Instance?

# For parsing command line arguments for a morphologizer
# -*- coding: utf-81 -*-

# General:

import argparse

class morphargs():
  def __init__(self):
    parser = argparse.ArgumentParser(
      prog = 'morphologizer',
      description='What it does',
      epilog = 'May the morph be with you.'
    )
    self.parser = parser

    parser.add_argument('langcode')  #
    parser.add('-v', '--verb')
    parser.add('-num', '--number')  # e.g., singular, dual, plural
    parser.add('-p', '--person')    # 1, 2, 3 or other?
    parser.add('-t', '--tense')     # present, imperfect, future simple, past perfect, etc.
    parser.add('-m', '--mode')      # indicative, subjunctive, imperative, infinitive, etc.
    parser.add('--adv', '--adverb')
    parser.add('--pass', '--passive')  # For passive voice

    parser.add('-s', '-subject')
    parser.add('-noun', '--noun')
    parser.add('-pn', '--pronoun')
    parser.add('--adj', '--adjective')

    parser.add('-do', '--directobject')
    parser.add('-io', '--indirectobject')

    parser.add('-prep', '--preposition')
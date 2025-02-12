#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys


# How have things been spelled here?
# The users will interact with this script purely in syllabary, they will not see that the backend
# is a mix of syllabary and transcription. However, to anyone who adds to or updates Morphy, the
# system used here is relevant (and I'm still hoping to simplify this further)
    
# When a vowel final element attaches to a vowel initial element...
# E.g. person prefix "iinii" [1D-inc-Sub/3S-inanimate-Obj] attaching to a vowel initial stem
# such as 'ookiska' ᎣᎩᏍᎦ''+[V]''+[PresCont]
# ...the final vowel drops. (the example above would be "iinookiska"). However, in Cherokee syllabary,
# each character represents a consonant and vowel combination, meaning that separate rules would be
# needed for each combination to successfully drop the correctvowel and attach the remaining consonant 
# to the remaining vowel.
# Therefore, final syllables of each component have been written in transctiption, allowing for all
# vowels to be dropped using a single rule. A set of rewrite rules then converts what is left at the
# end to syllabary. While still a lot of rules, this is significantly less than they would be if we
# started in syllabary. That said, I'm open to ideas on how else to approach this...
    


class chr_syllabary_fin():
    def __init__(self):

        # Person Prefixes

        # Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)
        setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "Ꮵ^"),
                    ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "Ꭲnii^"), \
                    ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "Ꭲtii^"), \
                    ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ᎣᏍtii^"), \
                    ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "Ꭳjii^"), \
                    ("'[2S-Sub/3S-inanimate-Obj]+'", "hi^"), \
                    ("'[2D-Sub/3S-inanimate-Obj]+'", "Ꮝtii^"), \
                    ("'[2P-Sub/3S-inanimate-Obj]+'", "Ꭲjii^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "a^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "ka^"), \
                    ("'[3P-Sub/3S-inanimate-Obj]+'", "Ꭰnii^")]

        setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ᎠᎩ^"), \
                    ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "Ꭹnii^"), \
                    ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "Ꭲkii^"), \
                    ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ᎣᎩnii^"), \
                    ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "Ꭳkii^"), \
                    ("'[2S-Sub/3S-inanimate-Obj]+'", "ja^"), \
                    ("'[2D-Sub/3S-inanimate-Obj]+'", "Ꮝtii^"), \
                    ("'[2P-Sub/3S-inanimate-Obj]+'", "Ꭲjii^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "Ꭴ^"), \
                    ("'[3P-Sub/3S-inanimate-Obj]+'", "Ꭴnii^")]

        # Transitive Verbs Only

        animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "Ꮵi^"), \
                       ("'[1D-inc-Sub/3S-animate-Obj]+'", "Ꭱnii^"), \
                       ("'[1P-inc-Sub/3S-animate-Obj]+'", "Ꭱtii^"), \
                       ("'[1D-ex-Sub/3S-animate-Obj]+'", "ᎣᏍtii^"), \
                       ("'[1P-ex-Sub/3S-animate-Obj]+'", "Ꭳjii^"), \
                       ("'[2S-Sub/3S-animate-Obj]+'", "Ꭿi^"), \
                    ("'[2D-Sub/3S-animate-Obj]+'", "ᎡᏍtii^"), \
                       ("'[2P-Sub/3S-animate-Obj]+'", "Ꭱjii^"), \
                       ("'[3S-Sub/3S-animate-Obj]+'", "a^"), \
                       ("'[3S-Sub/3S-animate-Obj]+'", "ka^"), \
                       ("'[3P-Sub/3S-animate-Obj]+'", "Ꭰnii^")]

        subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "ᎠᎩ^"), \
                      ("'[3S-Sub/1D-inc-Obj]+'", "Ꭹnii^"), \
                      ("'[3S-Sub/1P-inc-Obj]+'", "Ꭲkii^"), \
                      ("'[3S-Sub/1D-ex-Obj]+'", "ᎣᎩnii^"), \
                      ("'[3S-Sub/1P-ex-Obj]+'", "Ꭳkii^"), \
                      ("'[3S-Sub/2S-Obj]+'", "ja^"), \
                      ("'[3S-Sub/2D-Obj]+'", "Ꮝtii^"), \
                      ("'[3S-Sub/2P-Obj]+'", "Ꭲjii^")]

        subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "ᎬᎩ^"), \
                      ("'[3P-Sub/1D-inc-Obj]+'", "ᎨᎩnii^"), \
                      ("'[3P-Sub/1P-inc-Obj]+'", "Ꭸkii^"), \
                      ("'[3P-Sub/1D-ex-Obj]+'", "ᎪᎩnii^"), \
                      ("'[3P-Sub/1P-ex-Obj]+'", "Ꭺkii^"), \
                      ("'[3P-Sub/2S-Obj]+'", "Ꭸja^"), \
                      ("'[3P-Sub/2D-Obj]+'", "ᎨᏍtii^"), \
                      ("'[3P-Sub/2P-Obj]+'", "Ꭸjii^")]

        two_local = [("'[2S-Sub/1S-Obj]+'", "ᏍᎩ^"), \
             ("'[1S-Sub/2S-Obj]+'", "Ꭼ^"), \
             ("'[2S-Sub/1D-Obj]+'", "ᎢᏍᎩnii^"), \
             ("'[2D-Sub/1D-Obj]+'", "ᎢᏍᎩnii^"), \
             ("'[2D-Sub/1S-Obj]+'", "ᎢᏍᎩnii^"), \
             ("'[1S-Sub/2D-Obj]+'", "ᎢᏍᏛ^"), \
             ("'[1D-Sub/2D-Obj]+'", "ᎢᏍᏛ^"), \
             ("'[1D-Sub/2S-Obj]+'", "ᎢᏍᏛ^"),\
             ("'[2S-Sub/1P-Obj]+'", "ᎢᏍᎩi^"), \
             ("'[2D-Sub/1P-Obj]+'", "ᎢᏍᎩi^"), \
             ("'[2P-Sub/1P-Obj]+'", "ᎢᏍᎩi^"), \
             ("'[2P-Sub/1D-Obj]+'", "ᎢᏍᎩi^"), \
             ("'[2P-Sub/1S-Obj]+'", "ᎢᏍᎩi^"), \
             ("'[1S-Sub/2P-Obj]+'", "ᎢᏨ^"), \
             ("'[1D-Sub/2P-Obj]+'", "ᎢᏨ^"), \
             ("'[1P-Sub/2P-Obj]+'", "ᎢᏨ^"), \
             ("'[1P-Sub/2D-Obj]+'", "ᎢᏨ^"), \
             ("'[1P-Sub/2S-Obj]+'", "ᎢᏨ^")]

        object_focus = [("'[1S-inc-Obj]+'", "ᎥᎩ^"), \
                        ("'[1D-inc-Obj]+'", "ᎡᎩnii^"), \
                        ("'[1P-inc-Obj]+'", "Ꭱkii^"), \
                        ("'[1D-ex-Obj]+'", "ᎣᎩnii^"), \
                        ("'[1P-ex-Obj]+'", "Ꭳjii^"), \
                        ("'[2S-Obj]+'", "Ꭱja^"), \
                        ("'[2D-Obj]+'", "ᎡᏍtii^"), \
                        ("'[2P-Obj]+'", "Ꭱjii^"), \
                        ("'[3S-Obj]+'", "ᎠᏥ^"), \
                        ("'[3P-Obj]+'", "Ꭸjii^"), \
                        ("'[3P-Obj]+'", "Ꭸk^")]

    
        setA_tups = [(a, "SetA_Verbs") for a in setA_pre]
        setB_tups = [(b, "SetB_Verbs") for b in setB_pre]
        animate_obj_tups = [(c, "Transitive_Verbs") for c in animate_3SO]
        subj_3S_tups = [(d, "Transitive_Verbs") for d in subject_3S]
        subj_3P_tups = [(e, "Transitive_Verbs") for e in subject_3P]
        two_loc_tups = [(f, "Transitive_Verbs") for f in two_local]
        ob_foc_tups = [(g, "Transitive_Verbs") for g in object_focus]

        fin_person = setA_tups + setB_tups + animate_obj_tups + subj_3S_tups + subj_3P_tups + two_loc_tups + ob_foc_tups


        # Morpheme Concatenation. Currently includes:
        # 6 optionsal prepronominal prefixes (are attached before the person marker)
        # All person marking paradigms (required)
        # Verb stems (20 verbs, 5 stems each)
        # Present Continuous, Incompletive, Immediate, Completive, DeVerbal Noun/Infinitive forms
        # These are divided into Set A and Set B and Transitive and Intransitive, all of which affect the
        # type of person marking they can take
        # Final suffixes (required, specific suffix depends on type of verb stem)

        # 12 prepronominal prefixes in total (currently 6 have been implemented)
        # Titles Prefix1-7 indicate position of the prefixes in order if they cooccur
        # Prefixes within the same group cannot occur together
        # e.g. a verb cannot take both an irrealis (IRR) and a relativizer (REL)
        # There are also some long distance co-occurence restrictions
        # (e.g. verbs cannot take both REL and NGT prefixes)
        # Normally these would be handled using flag diacritics, but this functionality
        # is currently unavailable in pyfoma. Therefore, we will need to handle them through
        # our front-end interface instead
        
        Grammar = {}
        Grammar["S"] = [("", "Prefix1")]

        Grammar["Prefix1"] = [("", "Prefix2"), \
                              (("'[IRR]+'", "yi^"), "Prefix2"), \
                              (("'[REL]+'", "ji^"), "Prefix2"), \
                              (("'[NGI]+'", "jii^"), "Prefix2")]
        
        Grammar["Prefix2"] = [("", "Prefix3"), \
                              (("'[TRN]+'", "wi^"), "Prefix3")]

        Grammar["Prefix3"] = [("", "Prefix7"), \
                              (("'[PRT]+'", "ni^"), "Prefix7")]

        Grammar["Prefix7"] = [("", "PersonPrefixes"), \
                              (("'[NGT]+'", "kaa^"), "PersonPrefixes")]

        Grammar["PersonPrefixes"] = fin_person

        Grammar["SetA_Verbs"] = [("", "Intrans_SetA"), ("", "Trans_SetA")]
        Grammar["SetB_Verbs"] = [("", "Intrans_SetB"), ("", "Trans_SetB")]
        Grammar["Transitive_Verbs"] = [("", "Trans_SetA"), ("", "Trans_SetB")]


        # Verb Stems. The gloss always uses the present continuous form in syllabary. This is for 2 reasons:
        # Morphy can be called in transcription or in syllabary using the same gloss, do not have to
        # request the forms separately. We are assumiing that users will want to generate the finaal
        # Cherpkee words in syllabary, but that having a transcribed version with morpheme boundaries marked
        # alongside it will be useful for language learners
    
        # Each verb has 5 stem forms. While researchers have worked on finding a base stem that is then
        # altered to form each of the 5 forms, this has proven complicated, and the descriptive grammar
        # this script is based on simple treats them as 5 separate stems (and the Cherokee),
        # so I have done the same. However, if each stem was glosses in its actual form, users would
        # alreadt need to know what the different stem forms for a verb are in order to request it.
        # However, this should be the job of the morphologizer. So, we use the Present Continuous stem
        # as the 'base' form (the descriptive grammar treats this as the citation form, and the dictionary
        # uses the third person present continuous as its main verb listing). As long as users can ask for
        # that, they can then also select the actual form they want, e.g. Incompletive, and the correct
        # form will be generated.

        # Completive and DeVerbal Noun stems are always Set B,regardless of whether the other stems take Set A
        # or B prefixes

        # Another note on spelling:
        # Some verb stems (specifically the Incompletive, Completive, and DeVerbal Noun forms) end in a
        # consonant - when they attach to a final suffix, this consonant will combine with a vowel to make
        # a full syllable. However, that vowel depends on the suffix taken, and so is not included in the
        # stem. Syllabary does not allow for a consonant to be written alone (except /s/), and so these final
        # consonants are written in transcription, and rewrite rules convert them to full syllabary at the end.

        Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "ᏬᏂᎭ"), "#"), \
                                   (("'ᏬᏂᎭ''+[V]''+[Incompletive]'", "ᏬᏂᏍk"), "Habitual"), \
                                   (("'ᏬᏂᎭ''+[V]''+[Immediate]'", "ᏬᏂᎯ"), "#"), \
                                   (("'ᎠᎢ''+[V]''+[PresCont]'", "ᎠᎢ"), "#"), \
                                   (("'ᎠᎢ''+[V]''+[Incompletive]'", "ᎠᎢᏍ"), "Habitual"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "ᏅᏥᏙᎭ"), "#"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Incompletive]'", "ᏅᏥᏙh"), "Habitual"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Immediate]'", "ᏅᏥᏓ"), "#"), \
                                   (("'ᏪᏟᎭ''+[V]''+[PresCont]'", "ᏪᏟᎭ"), "#"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Incompletive]'", "ᏪᏟᏍk"), "Habitual"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Immediate]'", "ᏪᏢᎾ"), "#")]    

        Grammar["Intrans_SetB"] = [(("'ᏬᏂᎭ''+[V]''+[Completive]'", "ᏬᏂᏍ"), "Stem2and4Final"), \
                                   (("'ᏬᏂᎭ''+[V]''+[DeVerbalNoun]'", "ᏬᏂᎯᏍt"), "Stem5Final"), \
                                   (("'ᎠᎢ''+[V]''+[Completive]'", "ᎠᎢᏍ"), "Stem2and4Final"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "ᏅᏥᏙl"), "Stem2and4Final"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[DeVerbalNoun]'", "ᏅᏥᏓᏍt"), "Stem5Final"), \
                                   (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "ᎡᏡᎦ"), "#"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Incompletive]'", "ᎡᏡk"), "Habitual"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Immediate]'", "ᎡᏡᎲᎦ"), "#"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Completive]'", "ᎡᏡn"), "Stem2and4Final"), \
                                   (("'ᎡᏡᎦ''+[V]''+[DeVerbalNoun]'", "ᎡᏡᎲᏍt"), "Stem5Final"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[PresCont]'", "ᎪᏂᏲᎦ"), "#"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Incompletive]'", "ᎪᏂᏲk"), "Habitual"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Immediate]'", "ᎪᏂᏲᎩ"), "#"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Completive]'", "ᎪᏂᏲj"), "Stem2and4Final"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[DeVerbalNoun]'", "ᎪᏂᏲᏍt"), "Stem5Final"), \
                                   (("'ᎠᏂᎭ''+[V]''+[PresCont]'", "ᎠᏂᎭ"), "#"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Incompletive]'", "ᎠᏂh"), "Habitual"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Immediate]'", "ᎠᏂᎮᏍᏘ"), "#"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Completive]'", "ᎠᏂh"), "Stem2and4Final"), \
                                   (("'ᏲᎷᎭ''+[V]''+[PresCont]'", "ᏲᎷᎭ"), "#"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Incompletive]'", "ᏲᎷᏍ"), "Habitual"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Immediate]'", "ᏲᎷᎲᎦ"), "#"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Completive]'", "ᏲᎷᏍ"), "Stem2and4Final"), \
                                   (("'ᏲᎷᎭ''+[V]''+[DeVerbalNoun]'", "ᏲᎷt"), "Stem5Final"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[PresCont]'", "ᎵᏓᏍᏗᎭ"), "#"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Incompletive]'", "ᎵᏓᏍᏗᏍk"), "Habitual"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Immediate]'", "ᎵᏓᏍᏓ"), "#"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Completive]'", "ᎵᏓᏍᏔn"), "Stem2and4Final"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[DeVerbalNoun]'", "ᎵᏓᏍᏙt"), "Stem5Final"), \
                                   (("'ᏁᎫᏣ''+[V]''+[PresCont]'", "ᏁᎫᏣ"), "#"), \
                                   (("'ᏁᎫᏣ''+[V]''+[Incompletive]'", "ᏁᎫj"), "Habitual"), 
                                   (("'ᏁᎫᏣ''+[V]''+[Immediate]'", "ᏁᎫᏤᏍᏗ"), "#"), \
                                   (("'ᏁᎫᏣ''+[V]''+[Completive]'", "ᏁᎫj"), "Stem2and4Final"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Completive]'", "ᏪᏢn"), "Stem2and4Final"), \
                                   (("'ᏪᏟᎭ''+[V]''+[DeVerbalNoun]'", "ᏪᏢt"), "Stem5Final")]

        Grammar["Trans_SetA"] = [(("'ᏍᏕᎵᎭ''+[V]''+[PresCont]'", "ᏍᏕᎵᎭ"), "#"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[Incompletive]'", "ᏍᏕᎵᏍk"), "Habitual"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[Immediate]'", "ᏍᏕᎳ"), "#"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[PresCont]'", "ᎤᎢᎶᎠ"), "#"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Incompletive]'", "ᎤᎯᎶᏍk"), "Habitual"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Immediate]'", "ᎤᎯᎶᏣ"), "#"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[PresCont]'", "ᎣᎩᏍᎦ"), "#"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Incompletive]'", "ᎣᎦᏍk"), "Habitual"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Immediate]'", "ᎣᎩ"), "#"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[PresCont]'", "ᎥᏃᏌᏍᎦ"), "#"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Incompletive]'", "ᎥᏃᏌᏍk"), "Habitual"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Immediate]'", "ᎥᏃᏌ"), "#"), \
                                 (("'ᎥᏂᎭ''+[V]''+[PresCont]'", "ᎥᏂᎭ"), "#"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Incompletive]'", "ᎥᏂh"), "Habitual"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Immediate]'", "ᎥᏂᎦ"), "#"), 
                                 (("'ᏅᏆᎶᎠ''+[V]''+[PresCont]'", "ᏅᏆᎶᎠ"), "#"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[Incompletive]'", "ᏅᏆᎶᏍk"), "Habitual"), \
                                (("'ᏅᏆᎶᎠ''+[V]''+[Immediate]'", "ᏅᏆᎶᏣ"), "#")]

        Grammar["Trans_SetB"] = [(("'ᏍᏕᎵᎭ''+[V]''+[Completive]'", "ᏍᏕᎸh"), "Stem2and4Final"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[DeVerbalNoun]'", "ᏍᏕᎸt"), "Stem5Final"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Completive]'", "ᎤᎯᎶʔ"), "Stem2and4Final"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[DeverbalNoun]'", "ᎤᎯᎶᏍt"), "Stem5Final"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Completive]'", "ᎣᎦʔ"), "Stem2and4Final"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[DeVerbalNoun]'", "ᎣᎦᏍt"), "Stem5Final"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Completive]'", "ᎥᏃᏌh"), "Stem2and4Final"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[DeVerbalNoun]'", "ᎥᏃᏌᏍt"), "Stem5Final"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Completive]'", "ᎥᏂl"), "Stem2and4Final"), \
                                 (("'ᎥᏂᎭ''+[V]''+[DeVerbalNoun]'", "ᎥᏂᏍt"), "Stem5Final"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[PresCont]'", "ᎠᏚᎵᎭ"), "#"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[Incompletive]'", "ᎠᏚᎵᏍk"), "Habitual"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[Immediate]'", "ᎠᏚᎳ"), "#"), \
                         (("'ᎠᏚᎵᎭ''+[V]''+[Completive]'", "ᎠᏚᎸh"), "Stem2and4Final"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[DeVerbalNoun]'", "ᎠᏚᎸt"), "Stem5Final"), \
                                 (("'ᎠᏕᎦ''+[V]''+[PresCont]'", "ᎠᏕᎦ"), "#"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Incompletive]'", "ᎠᏕk"), "Habitual"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Immediate]'", "ᎠᏚᎦ"), "#"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Completive]'", "ᎠᏗᏅᏍ"), "Stem2and4Final"), \
                                 (("'ᎠᏕᎦ''+[V]''+[DeVerbalNoun]'", "ᎠᏗᏅt"), "Stem5Final"), \
                                 (("'ᎨᏳᎭ''+[V]''+[PresCont]'", "ᎨᏳᎭ"), "#"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Incompletive]'", "ᎨᏳᏍ"), "Habitual"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Immediate]'", "ᎨᏳᏎᏍᏗ"), "#"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Completive]'", "ᎨᏳᏍ"), "Stem2and4Final"), \
                                 (("'ᎨᏳᎭ''+[V]''+[DeVerbalNoun]'", "ᎨᏳt"), "Stem5Final"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[PresCont]'", "ᎠᏛᏓᏍᏗ"), "#"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Incompletive]'", "ᎠᏛᏓᏍt"), "Habitual"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Immediate]'", "ᎠᏛᏓᏍᏕᏍᏗ"), "#"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Completive]'", "ᎠᏛᏓᏍt"), "Stem2and4Final"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[DeVerbalNoun]'", "ᎠᏛᏓᏍᏙt"), "Stem5Final"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[Completive]'", "ᏅᏆᎶʔ"), "Stem2and4Final"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[DeVerbalNoun]'", "ᏅᏆᎶᏍt"), "Stem5Final")]

        # Final Suffixes (Required) - dependent on the verb stem
        # Present Continuous and Immediate stems do not take a final suffix
        # Incompletive stems can take either the habitual or one of the suffixes in Stem2and4Final
        # Completive stems take one of the suffixes in Stem2and4Final
        # Deverbal Noun/Infinitive stems take one of the suffixes in Stem5Final
        Grammar["Habitual"] = [(("'+[Habitual]'", "^ᎣᎢ"), "#"), \
                               ("", "Stem2and4Final")]

        Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^ᎥᎢ"), "#"), \
                                     (("'+[NonExpPast]'", "^ᎡᎢ"), "#"), \
                                     (("'+[AbsFut]'", "^ᎡᏍᏗ"), "#")]
        
        Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^Ꭲ"), "#"), \
                                 (("'+[NomAbility]'", "^ᎢᎢ"), "#")]

        # Turn the grammar defined above into an FST
        Lexicon = FST.rlg(Grammar, "S")
        Lexicon = Lexicon.epsilon_remove().determinize().minimize()


        # Rewrite Rules

        # Create list of fsts here, to be concatenated later
        fsts = {}
        fsts['V'] = FST.re("[aeiouvᎠᎡᎢᎣᎤᎥ]")         #  Vowels


        # Numbered Rules relate to person markers.
        # Rules 8 and 9 are for vowel dropping
        # NGT rules relate to the negative time prefix
        # TRN rules relate to the translocative prefix
        # Metathesis and aspiration are phonological processes that
        # occur when prefixes are attached in specific environments
        # Cleanup rules remove unwanted characters e.g. extra morpheme boundary markers (^) or added \?
        # Rules must be applied in the order below in order to work properly.

        rule1 = FST.re("$^rewrite(Ꮵ:k / _ \^ $V)", fsts)

        rule2 = FST.re("$^rewrite(i:y / [#|\^](Ꮵ|Ꭿ|ᎢᏍᎩ) _ \^ $V)", fsts)

        rule2_1 = FST.re("$^rewrite('':y / (Ꭼ|Ꮫ|Ꮸ) _ \^ $V)", fsts)

        rule3 = FST.re("$^rewrite(Ꭹ:(kw) / _ \^ $V)", fsts)

        
        # The transcription version of the script has 3 rules for metathesis, while there are
        # only 2 here. This is intentional, the differences in the writing systems necessitate this.
        metathesis1 = FST.re("$^rewrite((i\^h):(\^) / (y|w|n) _ )", fsts)
        metathesis2 = FST.re("$^rewrite(Ꭿ:'' / (y|w|n)i\^ _ )", fsts)

        # aspiration - transcription has 2 aspiration rules while here there is one, for the same reason
        # as metathesis. Also we may need to add more to these as more verbs, affixes, and complexity is added
        aspiration1 = FST.re("$^rewrite((ji\^h):(j\^))", fsts)
        aspiration2 = FST.re("$^rewrite((ji\^Ꭿ):(ji\^))", fsts)

        # Translocative Prefix (we, [TRN]+) --> yi -> yu and ji -> ju before (wi-)
        trn = FST.re("$^rewrite(i:u / (y|j) _ \^wi)", fsts)

        # NGT Rules
        # kaa + uu = kvv^wa 
        ngt1 = FST.re("$^rewrite((kaa\^Ꭴ):(Ꭼ\^wa))", fsts)

        # kvv^wa^ + v = kvv^wa^
        ngt2 = FST.re("$^rewrite(Ꭵ:'' / Ꭼ\^wa\^ _ )", fsts)

        # Kaa + aji (ᎠᏥ^) = k^eji
        ngt3 = FST.re("$^rewrite(Ꭰ:Ꭱ / kaa\^ _ (Ꮵ|k)\^ )", fsts)

        # Kaa + [eiov] = kaay^ + [eiov]
        ngt4 = FST.re("$^rewrite((kaa):(Ꭶy) / _ \^ [eiovᎡᎢᎣᎥ])", fsts)

        # Kaa + a = kvv^
        ngt5 = FST.re("$^rewrite((kaa\^(aa?|Ꭰ)):(kvv\^), longest = True, leftmost = True)", fsts)

        # uu (SetB [3S-Sub/3S-inanimate-Obj])
        rule4 = FST.re("$^rewrite('':w / Ꭴ _ \^ [eouᎡᎣᎤ])", fsts)

        rule5 = FST.re("$^rewrite((Ꭴ\^Ꭵ):(ᎤᏩ\^))", fsts)
        # Syllabary to syllabary

        rule6 = FST.re("$^rewrite(Ꭰ:'' / Ꭴ\^ _ )", fsts)
        # uu will be in syllabary, a will not

        # rule7 --> Add later
        cleanup1 = FST.re("$^rewrite(\^:'' / \^ _)", fsts)

        rule8 = FST.re("$^rewrite((aa?|ii?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)
        rule9 = FST.re("$^rewrite((vv?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)

        self.rules =[
            rule1, rule2, rule2_1, rule3,
            rule4, rule5, rule6, rule8, rule9
        ]
        cleanup2 = FST.re("$^rewrite(\^:'')")
        
        # Rules to convert any remaining transcription into syllabary.
        
        # kw -> vowel
        fsts['kw_a'] = FST.re("$^rewrite((kwᎠ|kwaa?):Ꮖ, longest = True, leftmost = True)", fsts)
        fsts['kw_e'] = FST.re("$^rewrite((kwᎡ|kwee?):Ꮗ, longest = True, leftmost = True)", fsts)
        fsts['kw_i'] = FST.re("$^rewrite((kwᎢ|kwii?):Ꮘ, longest = True, leftmost = True)", fsts)
        fsts['kw_o'] = FST.re("$^rewrite((kwᎣ|kwoo?):Ꮙ, longest = True, leftmost = True)", fsts)
        fsts['kw_u'] = FST.re("$^rewrite((kwᎤ|kwuu?):Ꮚ, longest = True, leftmost = True)", fsts)
        fsts['kw_v'] = FST.re("$^rewrite((kwᎥ|kwvv?):Ꮛ, longest = True, leftmost = True)", fsts)
        
        # k -> vowel
        fsts['k_a'] = FST.re("$^rewrite((kᎠ|kaa?):Ꭶ, longest = True, leftmost = True)", fsts)
        fsts['k_e'] = FST.re("$^rewrite((kᎡ|kee?):Ꭸ, longest = True, leftmost = True)", fsts)
        fsts['k_i'] = FST.re("$^rewrite((kᎢ|kii?):Ꭹ, longest = True, leftmost = True)", fsts)
        fsts['k_o'] = FST.re("$^rewrite((kᎣ|koo?):Ꭺ, longest = True, leftmost = True)", fsts)
        fsts['k_u'] = FST.re("$^rewrite((kᎤ|kuu?):Ꭻ, longest = True, leftmost = True)", fsts)
        fsts['k_v'] = FST.re("$^rewrite((kᎥ|kvv?):Ꭼ, longest = True, leftmost = True)", fsts)

        # y -> vowel
        fsts['y_a'] = FST.re("$^rewrite((yᎠ|yaa?):Ꮿ, longest = True, leftmost = True)", fsts)
        fsts['y_e'] = FST.re("$^rewrite((yᎡ|yee?):Ᏸ, longest = True, leftmost = True)", fsts)
        fsts['y_i'] = FST.re("$^rewrite((yᎢ|yii?):Ᏹ, longest = True, leftmost = True)", fsts)
        fsts['y_o'] = FST.re("$^rewrite((yᎣ|yoo?):Ᏺ, longest = True, leftmost = True)", fsts)
        fsts['y_u'] = FST.re("$^rewrite((yᎤ|yuu?):Ᏻ, longest = True, leftmost = True)", fsts)
        fsts['y_v'] = FST.re("$^rewrite((yᎥ|yvv?):Ᏼ, longest = True, leftmost = True)", fsts)

        # j -> vowel
        fsts['j_a'] = FST.re("$^rewrite((jᎠ|jaa?):Ꮳ, longest = True, leftmost = True)", fsts)
        fsts['j_e'] = FST.re("$^rewrite((jᎡ|jee?):Ꮴ, longest = True, leftmost = True)", fsts)
        fsts['j_i'] = FST.re("$^rewrite((jᎢ|jii?):Ꮵ, longest = True, leftmost = True)", fsts)
        fsts['j_o'] = FST.re("$^rewrite((jᎣ|joo?):Ꮶ, longest = True, leftmost = True)", fsts)
        fsts['j_u'] = FST.re("$^rewrite((jᎤ|juu?):Ꮷ, longest = True, leftmost = True)", fsts)
        fsts['j_v'] = FST.re("$^rewrite((jᎥ|jvv?):Ꮸ, longest = True, leftmost = True)", fsts)

        # w -> vowel
        fsts['w_a'] = FST.re("$^rewrite((wᎠ|waa?):Ꮹ, longest = True, leftmost = True)", fsts)
        fsts['w_e'] = FST.re("$^rewrite((wᎡ|wee?):Ꮺ, longest = True, leftmost = True)", fsts)
        fsts['w_i'] = FST.re("$^rewrite((wᎢ|wii?):Ꮻ, longest = True, leftmost = True)", fsts)
        fsts['w_o'] = FST.re("$^rewrite((wᎣ|woo?):Ꮼ, longest = True, leftmost = True)", fsts)
        fsts['w_u'] = FST.re("$^rewrite((wᎤ|wuu?):Ꮽ, longest = True, leftmost = True)", fsts)
        fsts['w_v'] = FST.re("$^rewrite((wᎥ|wvv?):Ꮾ, longest = True, leftmost = True)", fsts)

        # n -> vowel
        fsts['n_a'] = FST.re("$^rewrite((nᎠ|naa?):Ꮎ, longest = True, leftmost = True)", fsts)
        fsts['n_e'] = FST.re("$^rewrite((nᎡ|nee?):Ꮑ, longest = True, leftmost = True)", fsts)
        fsts['n_i'] = FST.re("$^rewrite((nᎢ|nii?):Ꮒ, longest = True, leftmost = True)", fsts)
        fsts['n_o'] = FST.re("$^rewrite((nᎣ|noo?):Ꮓ, longest = True, leftmost = True)", fsts)
        fsts['n_u'] = FST.re("$^rewrite((nᎤ|nuu?):Ꮔ, longest = True, leftmost = True)", fsts)
        fsts['n_v'] = FST.re("$^rewrite((nᎥ|nvv?):Ꮕ, longest = True, leftmost = True)", fsts)

        # t -> vowel
        fsts['t_a'] = FST.re("$^rewrite((tᎠ|taa?):Ꮣ, longest = True, leftmost = True)", fsts)
        fsts['t_e'] = FST.re("$^rewrite((tᎡ|tee?):Ꮥ, longest = True, leftmost = True)", fsts)
        fsts['t_i'] = FST.re("$^rewrite((tᎢ|tii?):Ꮧ, longest = True, leftmost = True)", fsts)
        fsts['t_o'] = FST.re("$^rewrite((tᎣ|too?):Ꮩ, longest = True, leftmost = True)", fsts)
        fsts['t_u'] = FST.re("$^rewrite((tᎤ|tuu?):Ꮪ, longest = True, leftmost = True)", fsts)
        fsts['t_v'] = FST.re("$^rewrite((tᎥ|tvv?):Ꮫ, longest = True, leftmost = True)", fsts)

        # h -> vowel
        fsts['h_a'] = FST.re("$^rewrite((hᎠ|haa?):Ꭽ, longest = True, leftmost = True)", fsts)
        fsts['h_e'] = FST.re("$^rewrite((hᎡ|hee?):Ꭾ, longest = True, leftmost = True)", fsts)
        fsts['h_i'] = FST.re("$^rewrite((hᎢ|hii?):Ꭿ, longest = True, leftmost = True)", fsts)
        fsts['h_o'] = FST.re("$^rewrite((hᎣ|hoo?):Ꮀ, longest = True, leftmost = True)", fsts)
        fsts['h_u'] = FST.re("$^rewrite((hᎤ|huu?):Ꮁ, longest = True, leftmost = True)", fsts)
        fsts['h_v'] = FST.re("$^rewrite((hᎥ|hvv?):Ꮂ, longest = True, leftmost = True)", fsts)

        # Ꮝ -> vowel
        fsts['Ꮝ_e'] = FST.re("$^rewrite((ᏍᎡ|Ꮝee?):Ꮞ, longest = True, leftmost = True)", fsts)
        fsts['Ꮝ_o'] = FST.re("$^rewrite((ᏍᎣ|Ꮝoo?):Ꮠ, longest = True, leftmost = True)", fsts)
        fsts['Ꮝ_v'] = FST.re("$^rewrite((ᏍᎥ|Ꮝvv?):Ꮢ, longest = True, leftmost = True)", fsts)

        # l -> vowel
        fsts['l_e'] = FST.re("$^rewrite((lᎡ|lee?):Ꮄ, longest = True, leftmost = True)", fsts)
        fsts['l_v'] = FST.re("$^rewrite((lᎥ|lvv?):Ꮈ, longest = True, leftmost = True)", fsts)

        # Drop any stray i and ʔ
        fsts['drops'] = FST.re("$^rewrite((i|ʔ):'')", fsts)



        fsts['Lexicon'] = Lexicon
        fsts['rule1'] = rule1
        fsts['rule2'] = rule2
        fsts['rule2_1'] = rule2_1
        fsts['rule3'] = rule3
        fsts['metathesis1'] = metathesis1
        fsts['metathesis2'] = metathesis2
        fsts['aspiration1'] = aspiration1
        fsts['aspiration2'] = aspiration2
        fsts['trn'] = trn
        fsts['ngt1'] = ngt1
        fsts['ngt2'] = ngt2
        fsts['ngt3'] = ngt3
        fsts['ngt4'] = ngt4
        fsts['ngt5'] = ngt5
        fsts['rule4'] = rule4
        fsts['rule5'] = rule5
        fsts['rule6'] = rule6
        fsts['cleanup1'] = cleanup1
        fsts['rule8'] = rule8
        fsts['rule9'] = rule9
        fsts['cleanup2'] = cleanup2
        fsts['kw'] = FST.re("$kw_a @ $kw_e @ $kw_i @ $kw_o @ $kw_u @ $kw_v", fsts)
        fsts['k'] = FST.re("$k_a @ $k_e @ $k_i @ $k_o @ $k_u @ $k_v", fsts)
        fsts['y'] = FST.re("$y_a @ $y_e @ $y_i @ $y_o @ $y_u @ $y_v", fsts)
        fsts['j'] = FST.re("$j_a @ $j_e @ $j_i @ $j_o @ $j_u @ $j_v", fsts)
        fsts['w'] = FST.re("$w_a @ $w_e @ $w_i @ $w_o @ $w_u @ $w_v", fsts)
        fsts['n'] = FST.re("$n_a @ $n_e @ $n_i @ $n_o @ $n_u @ $n_v", fsts)
        fsts['t'] = FST.re("$t_a @ $t_e @ $t_i @ $t_o @ $t_u @ $t_v", fsts)
        fsts['h'] = FST.re("$h_a @ $h_e @ $h_i @ $h_o @ $h_u @ $h_v", fsts)
        fsts['Ꮝ'] = FST.re("$Ꮝ_e @ $Ꮝ_o @ $Ꮝ_v", fsts)
        fsts['l'] = FST.re("$l_e @ $l_v", fsts)

        self.final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $aspiration1 @ $aspiration2 @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $rule8 @ $rule9 @ $cleanup2 @ $kw @ $k @ $y @ $j @ $w @ $n @ $t @ $h @ $Ꮝ @ $l @ $drops", fsts)

    def generate(self, text):
        result = list(self.final.generate(text))
        if not result:
            result = "-- undefined --"
        return result

    def parse(self, text):
        result = list(self.final.analyze(text))
        if not result:
            result = "-- undefined --"
        return result
    

def main(argv):
    morpher = chr_syllabary_fin()
    function = sys.argv[1]
    cherokee = sys.argv[2]
    if function == 'generate':
        res = list(morpher.generate(cherokee))
    elif function == 'parse':
        res = list(morpher.analyze(cherokee))
    else:
        res = "Arg1 must be either 'generate' or 'parse'"
    return res


if __name__ == "main":
    result = main(sys.argv)
    print(result)

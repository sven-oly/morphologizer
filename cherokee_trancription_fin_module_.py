#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys


class chr_transcript_fin():
    def __init__(self):
        #Person Prefixes - these attach to the verb stem and are required

        #Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)
        setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ji^"), \
                    ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "iinii^"), \
                    ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iitii^"), \
                    ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "oostii^"), \
                    ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "oojii^"), \
                    ("'[2S-Sub/3S-inanimate-Obj]+'", "hi^"), \
                    ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
                    ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "a^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "ka^"), \
                    ("'[3P-Sub/3S-inanimate-Obj]+'", "anii^")]

        setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "aki^"), \
                    ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "kinii^"), \
                    ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iikii^"), \
                    ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ookinii^"), \
                    ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "ookii^"), \
                    ("'[2S-Sub/3S-inanimate-Obj]+'", "ja^"), \
                    ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
                    ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), \
                    ("'[3S-Sub/3S-inanimate-Obj]+'", "uu^"), \
                    ("'[3P-Sub/3S-inanimate-Obj]+'", "uunii^")]

        #Transitive Verbs Only
        animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "jii^"), \
                       ("'[1D-inc-Sub/3S-animate-Obj]+'", "eenii^"), \
                       ("'[1P-inc-Sub/3S-animate-Obj]+'", "eetii^"), \
                       ("'[1D-ex-Sub/3S-animate-Obj]+'", "oostii^"), \
                       ("'[1P-ex-Sub/3S-animate-Obj]+'", "oojii^"), \
                       ("'[2S-Sub/3S-animate-Obj]+'", "hii^"), \
                       ("'[2D-Sub/3S-animate-Obj]+'", "eestii^"), \
                       ("'[2P-Sub/3S-animate-Obj]+'", "eejii^"), \
                       ("'[3S-Sub/3S-animate-Obj]+'", "a^"), \
                       ("'[3S-Sub/3S-animate-Obj]+'", "ka^"), \
                       ("'[3P-Sub/3S-animate-Obj]+'", "anii^")]

        subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "aki^"), \
                      ("'[3S-Sub/1D-inc-Obj]+'", "kinii^"), \
                      ("'[3S-Sub/1P-inc-Obj]+'", "iikii^"), \
                      ("'[3S-Sub/1D-ex-Obj]+'", "ookinii^"), \
                      ("'[3S-Sub/1P-ex-Obj]+'", "ookii^"), \
                      ("'[3S-Sub/2S-Obj]+'", "ja^"), \
                      ("'[3S-Sub/2D-Obj]+'", "stii^"), \
                      ("'[3S-Sub/2P-Obj]+'", "iijii^")]

        subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "kvvki^"), \
                      ("'[3P-Sub/1D-inc-Obj]+'", "keekinii^"), \
                      ("'[3P-Sub/1P-inc-Obj]+'", "keekii^"), \
                      ("'[3P-Sub/1D-ex-Obj]+'", "kookinii^"), \
                      ("'[3P-Sub/1P-ex-Obj]+'", "kookii^"), \
                      ("'[3P-Sub/2S-Obj]+'", "keeja^"), \
                      ("'[3P-Sub/2D-Obj]+'", "keestii^"), \
                      ("'[3P-Sub/2P-Obj]+'", "keejii^")]

        two_local = [("'[2S-Sub/1S-Obj]+'", "ski^"), \
                     ("'[1S-Sub/2S-Obj]+'", "kvv^"), \
                     ("'[2S-Sub/1D-Obj]+'", "iiskinii^"), \
                     ("'[2D-Sub/1D-Obj]+'", "iiskinii^"), \
                     ("'[2D-Sub/1S-Obj]+'", "iiskinii^"), \
                     ("'[1S-Sub/2D-Obj]+'", "iistvv^"), \
                     ("'[1D-Sub/2D-Obj]+'", "iistvv^"), \
                     ("'[1D-Sub/2S-Obj]+'", "iistvv^"),\
                     ("'[2S-Sub/1P-Obj]+'", "iiskii^"), \
                     ("'[2D-Sub/1P-Obj]+'", "iiskii^"), \
                     ("'[2P-Sub/1P-Obj]+'", "iiskii^"), \
                     ("'[2P-Sub/1D-Obj]+'", "iiskii^"), \
                     ("'[2P-Sub/1S-Obj]+'", "iiskii^"), \
                     ("'[1S-Sub/2P-Obj]+'", "iijvv^"), \
                     ("'[1D-Sub/2P-Obj]+'", "iijvv^"), \
                     ("'[1P-Sub/2P-Obj]+'", "iijvv^"), \
                     ("'[1P-Sub/2D-Obj]+'", "iijvv^"), \
                     ("'[1P-Sub/2S-Obj]+'", "iijvv^")]

        object_focus = [("'[1S-inc-Obj]+'", "vvki^"), \
                        ("'[1D-inc-Obj]+'", "eekinii^"), \
                        ("'[1P-inc-Obj]+'", "eekii^"), \
                        ("'[1D-ex-Obj]+'", "ookinii^"), \
                        ("'[1P-ex-Obj]+'", "oojii^"), \
                        ("'[2S-Obj]+'", "eeja^"), \
                        ("'[2D-Obj]+'", "eestii^"), \
                        ("'[2P-Obj]+'", "eejii^"), \
                        ("'[3S-Obj]+'", "aji^"), \
                        ("'[3P-Obj]+'", "keejii^"), \
                        ("'[3P-Obj]+'", "keek^")]


        setA_tups = [(a, "SetA_Verbs") for a in setA_pre]
        setB_tups = [(b, "SetB_Verbs") for b in setB_pre]
        animate_obj_tups = [(c, "Transitive_Verbs") for c in animate_3SO]
        subj_3S_tups = [(d, "Transitive_Verbs") for d in subject_3S]
        subj_3P_tups = [(e, "Transitive_Verbs") for e in subject_3P]
        two_loc_tups = [(f, "Transitive_Verbs") for f in two_local]
        ob_foc_tups = [(g, "Transitive_Verbs") for g in object_focus]



        fin_person = setA_tups + setB_tups + animate_obj_tups + subj_3S_tups + subj_3P_tups + two_loc_tups + ob_foc_tups

        #Morpheme Concatenation. Currently includes:
        #6 optionsal prepronominal prefixes (are attached before the person marker)
        #All person marking paradigms (required)
        #Verb stems (20 verbs, 5 stems each)
        #Present Continuous, Incompletive, Immediate, Completive, DeVerbal Noun/Infinitive forms
        #These are divided into Set A and Set B and Transitive and Intransitive, all of which affect the
        #type of person marking they can take
        #Final suffixes (required, specific suffix depends on type of verb stem)

        Grammar = {}
        Grammar["S"] = [("", "Prefix1")]

        #12 prepronominal prefixes in total (currently 6 have been implemented)
        #Titles Prefix1-7 indicate position of the prefixes in order if they cooccur
        #Prefixes within the same group cannot occur together
        #e.g. a verb cannot take both an irrealis (IRR) and a relativizer (REL)
        #There are also some long distance co-occurence restrictions
        #(e.g. verbs cannot take both REL and NGT prefixes)
        #Normally these would be handled using flag diacritics, but this functionality
        #is currently unavailable in pyfoma. Therefore, we will need to handle them through
        #our front-end interface instead
        Grammar["Prefix1"] = [("", "Prefix2"), \
                              (("'[IRR]+'", "yi^"), "Prefix2"), \
                              (("'[REL]+'", "j?i^"), "Prefix2"), \
                              (("'[NGI]+'", "?jii^"), "Prefix2")]

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

        #Verb Stems. The gloss always uses the present continuous form in syllabary. This is for 2 reasons:
        #Morphy can be called in transcription or in syllabary using the same gloss, do not have to
        #request the forms separately. We are assumiing that users will want to generate the finaal
        #Cherpkee words in syllabary, but that having a transcribed version with morpheme boundaries marked
        #alongside it will be useful for language learners

            #Each verb has 5 stem forms. While researchers have worked on finding a base stem that is then
            #altered to form each of the 5 forms, this has proven complicated, and the descriptive grammar
            #this script is based on simple treats them as 5 separate stems (and the Cherokee),
            #so I have done the same. However, if each stem was glosses in its actual form, users would
            #alreadt need to know what the different stem forms for a verb are in order to request it.
            #However, this should be the job of the morphologizer. So, we use the Present Continuous stem
            #as the 'base' form (the descriptive grammar treats this as the citation form, and the dictionary
            #uses the third person present continuous as its main verb listing). As long as users can ask for
            #that, they can then also select the actual form they want, e.g. Incompletive, and the correct
            #form will be generated.

        #Completive and DeVerbal Noun stems are always Set B,regardless of whether the other stems take Set A
        #or B prefixes

        Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "wooniha"), "#"), \
                                   (("'ᏬᏂᎭ''+[V]''+[Incompletive]'", "woonisk"), "Habitual"), \
                                   (("'ᏬᏂᎭ''+[V]''+[Immediate]'", "woonihi"), "#"), \
                                   (("'ᎠᎢ''+[V]''+[PresCont]'", "aaʔi"), "#"), \
                                   (("'ᎠᎢ''+[V]''+[Incompletive]'", "aaɁis"), "Habitual"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "nvvjiitooha"), "#"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Incompletive]'", "nvvjiitooh"), "Habitual"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Immediate]'", "nvvjiita"), "#"), \
                                   (("'ᏪᏟᎭ''+[V]''+[PresCont]'", "weehliha"), "#"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Incompletive]'", "weehliisk"), "Habitual"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Immediate]'", "weehlvvna"), "#")]

        Grammar["Intrans_SetB"] = [(("'ᏬᏂᎭ''+[V]''+[Completive]'", "woonis"), "Stem2and4Final"), \
                                   (("'ᏬᏂᎭ''+[V]''+[DeVerbalNoun]'", "woonihist"), "Stem5Final"), \
                                   (("'ᎠᎢ''+[V]''+[Completive]'", "aaɁis"), "Stem2and4Final"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "nvvjiitool"), "Stem2and4Final"), \
                                   (("'ᏅᏥᏙᎭ''+[V]''+[DeVerbalNoun]'", "nvvjiitaast"), "Stem5Final"), \
                                   (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "eehluuhka"), "#"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Incompletive]'", "eehluuhk"), "Habitual"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Immediate]'", "eehluhvvka"), "#"), \
                                   (("'ᎡᏡᎦ''+[V]''+[Completive]'", "eehluhn"), "Stem2and4Final"), \
                                   (("'ᎡᏡᎦ''+[V]''+[DeVerbalNoun]'", "eehluhvst"), "Stem5Final"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[PresCont]'", "koohniiyooka"), "#"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Incompletive]'", "koohniiyook"), "Habitual"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Immediate]'", "koohniiyooki"), "#"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[Completive]'", "koohniiyooj"), "Stem2and4Final"), \
                                   (("'ᎪᏂᏲᎦ''+[V]''+[DeVerbalNoun]'", "koohniiyost"), "Stem5Final"), \
                                   (("'ᎠᏂᎭ''+[V]''+[PresCont]'", "aahniha"), "#"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Incompletive]'", "aahnih"), "Habitual"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Immediate]'", "aahniheesti"), "#"), \
                                   (("'ᎠᏂᎭ''+[V]''+[Completive]'", "aahnih"), "Stem2and4Final"), \
                                   (("'ᏲᎷᎭ''+[V]''+[PresCont]'", "hyooluha"), "#"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Incompletive]'", "hyooluus"), "Habitual"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Immediate]'", "hyooluuhvvka"), "#"), \
                                   (("'ᏲᎷᎭ''+[V]''+[Completive]'", "hyooluus"), "Stem2and4Final"), \
                                   (("'ᏲᎷᎭ''+[V]''+[DeVerbalNoun]'", "hyooluuht"), "Stem5Final"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[PresCont]'", "liitaastiha"), "#"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Incompletive]'", "liitaastiisk"), "Habitual"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Immediate]'", "liitaasta"), "#"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[Completive]'", "liitaasthan"), "Stem2and4Final"), \
                                   (("'ᎵᏓᏍᏗᎭ''+[V]''+[DeVerbalNoun]'", "liitaastooht"), "Stem5Final"), \
                                   (("'ᏁᎫᏣ''+[V]''+[PresCont]'", "neekuujaa"), "#"), \
                                   (("'ᏁᎫᏣ''+[V]''+[Incompletive]'", "neekuuj"), "Habitual"), 
                                   (("'ᏁᎫᏣ''+[V]''+[Immediate]'", "neekuujeesti"), "#"), \
                                   (("'ᏁᎫᏣ''+[V]''+[Completive]'", "neekuuj"), "Stem2and4Final"), \
                                   (("'ᏪᏟᎭ''+[V]''+[Completive]'", "weehlvvhn"), "Stem2and4Final"), \
                                   (("'ᏪᏟᎭ''+[V]''+[DeVerbalNoun]'", "weehlvvht"), "Stem5Final")]

        Grammar["Trans_SetA"] = [(("'ᏍᏕᎵᎭ''+[V]''+[PresCont]'", "steeliha"), "#"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[Incompletive]'", "steeliisk"), "Habitual"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[Immediate]'", "steela"), "#"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[PresCont]'", "uʔiilooʔa"), "#"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Incompletive]'", "uuhiiloosk"), "Habitual"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Immediate]'", "uuhiilooja"), "#"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[PresCont]'", "ookiska"), "#"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Incompletive]'", "ookask"), "Habitual"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Immediate]'", "ookii"), "#"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[PresCont]'", "vvnoosaska"), "#"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Incompletive]'", "vvnoosask"), "Habitual"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Immediate]'", "vvnoosa"), "#"), \
                                 (("'ᎥᏂᎭ''+[V]''+[PresCont]'", "vvhniha"), "#"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Incompletive]'", "vvhnih"), "Habitual"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Immediate]'", "vvnika"), "#"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[PresCont]'", "nvvkwalooɁa"), "#"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[Incompletive]'", "nvvkwaloosk"), "Habitual"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[Immediate]'", "nvvkwalooja"), "#")]

        Grammar["Trans_SetB"] = [(("'ᏍᏕᎵᎭ''+[V]''+[Completive]'", "steelvvh"), "Stem2and4Final"), \
                                 (("'ᏍᏕᎵᎭ''+[V]''+[DeVerbalNoun]'", "stehlt"), "Stem5Final"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[Completive]'", "uuhiilooʔ"), "Stem2and4Final"), \
                                 (("'ᎤᎢᎶᎠ''+[V]''+[DeVerbalNoun]'", "uuhiiloost"), "Stem5Final"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[Completive]'", "ookaʔ"), "Stem2and4Final"), \
                                 (("'ᎣᎩᏍᎦ''+[V]''+[DeVerbalNoun]'", "ookast"), "Stem5Final"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[Completive]'", "vvnoosah"), "Stem2and4Final"), \
                                 (("'ᎥᏃᏌᏍᎦ''+[V]''+[DeVerbalNoun]'", "vvnoosast"), "Stem5Final"), \
                                 (("'ᎥᏂᎭ''+[V]''+[Completive]'", "vvhnil"), "Stem2and4Final"), \
                                 (("'ᎥᏂᎭ''+[V]''+[DeVerbalNoun]'", "vvnst"), "Stem2and4Final"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[PresCont]'", "atuuliha"), "#"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[Incompletive]'", "atuulisk"), "Habitual"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[Immediate]'", "atuula"), "#"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[Completive]'", "atuulvvh"), "Stem2and4Final"), \
                                 (("'ᎠᏚᎵᎭ''+[V]''+[DeVerbalNoun]'", "atuuhlt"), "Stem5Final"), \
                                 (("'ᎠᏕᎦ''+[V]''+[PresCont]'", "ateeka"), "#"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Incompletive]'", "ateek"), "Habitual"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Immediate]'", "atuuka"), "#"), \
                                 (("'ᎠᏕᎦ''+[V]''+[Completive]'", "atiinvvs"), "Stem2and4Final"), \
                                 (("'ᎠᏕᎦ''+[V]''+[DeVerbalNoun]'", "atiinvvt"), "Stem5Final"), \
                                 (("'ᎨᏳᎭ''+[V]''+[PresCont]'", "keeyuha"), "#"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Incompletive]'", "keeyus"), "Habitual"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Immediate]'", "keeyuseesti"), "#"), \
                                 (("'ᎨᏳᎭ''+[V]''+[Completive]'", "keeyus"), "Stem2and4Final"), \
                                 (("'ᎨᏳᎭ''+[V]''+[DeVerbalNoun]'", "keeyhdt"), "Stem5Final"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[PresCont]'", "aathvvtaastii"), "#"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Incompletive]'", "aathvvtaast"), "Habitual"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Immediate]'", "aathvvtaasteesti"), "#"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[Completive]'", "aathvvtaast"), "Stem2and4Final"), \
                                 (("'ᎠᏛᏓᏍᏗ''+[V]''+[DeVerbalNoun]'", "aathvvtaastooht"), "Stem5Final"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[Completive]'", "nvvkwalooɁ"), "Stem2and4Final"), \
                                 (("'ᏅᏆᎶᎠ''+[V]''+[DeVerbalNoun]'", "nvvkwaloost"), "Stem5Final")]

        #Final Suffixes (Required) - dependent on the verb stem
        #Present Continuous and Immediate stems do not take a final suffix
        #Incompletive stems can take either the habitual or one of the suffixes in Stem2and4Final
        #Completive stems take one of the suffixes in Stem2and4Final
        #Deverbal Noun/Infinitive stems take one of the suffixes in Stem5Final
        Grammar["Habitual"] = [(("'+[Habitual]'", "^oʔi"), "#"), \
                               ("", "Stem2and4Final")]
        Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^vvʔi"), "#"), \
                                     (("'+[NonExpPast]'", "^eʔi"), "#"), \
                                     (("'+[AbsFut]'", "^éesti"), "#")]
        Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^i"), "#"), \
                                 (("'+[NomAbility]'", "^ííʔi"), "#")]


        #Turn the grammar defined above into an FST
        Lexicon = FST.rlg(Grammar, "S")
        Lexicon = Lexicon.epsilon_remove().determinize().minimize()

        #Create list of fsts here, to be concatenated later
        fsts = {}
        fsts['V'] = FST.re("[aeiouv]")         # Vowels

        #Numbered Rules relate to person markers.
        #Rules 8 and 9 are for vowel dropping
        #NGT rules relate to the negative time prefix
        #TRN rules relate to the translocative prefix
        #Metathesis and aspiration are phonological processes that
        #occur when prefixes are attached in specific environments
        #Cleanup rules remove unwanted characters e.g. extra morpheme boundary markers (^) or added \?
        #Rules must be applied in the order below in order to work properly.

        rule1 = FST.re("$^rewrite((ji):k / _ \^ $V)", fsts)

        rule2 = FST.re("$^rewrite('':y / [#|\^](j|h|iisk)ii _ \^ $V)", fsts)

        #kvv-, iistvv-, iijvv
        rule2_1 = FST.re("$^rewrite('':y / (k|t|j)vv _ \^ $V)", fsts)

        rule3 = FST.re("$^rewrite((ki):(kw) / _ \^ $V)", fsts)

        #Metathesis with /h/ --> Yi^h -> hy^, wi^h -> hw^, ni^h -> hn^
        metathesis1 = FST.re("$^rewrite((yi\^h):(hy\^))", fsts)
        metathesis2 = FST.re("$^rewrite((wi\^h):(hw\^))", fsts)
        metathesis3 = FST.re("$^rewrite((ni\^h):(hn\^))", fsts)

        #aspiration (ji^h -> ch^)
        aspiration = FST.re("$^rewrite((j\?i\^h):(ch\^))", fsts)

        #Translocative Prefix (wi, [TRN]+) affects IRR and REL: yi -> yu and ji -> ju before (wi-)
        trn = FST.re("$^rewrite(i:u / (y|j\?) _ \^wi)", fsts)


        #Negative Time Prefix (kaa, [NGT]+) rules

        #kaa + uu = kvv^wa 
        ngt1 = FST.re("$^rewrite((kaa\^uu):(kvv\^wa))", fsts)

        #kvv^wa^ + v = kvv^wa^
        ngt2 = FST.re("$^rewrite((vv?):'' / kvv\^wa\^ _ , longest = True, leftmost = True)", fsts)

        #Kaa + aji = k^eji
        ngt3 = FST.re("$^rewrite(a:e / kaa\^ _ (ji|k)\^ )", fsts)

        #Kaa + [eiov] = kaay^ + [eiov]
        ngt4 = FST.re("$^rewrite('':y / kaa _ \^ [eiov])", fsts)

        #Kaa + a = kvv^
        ngt5 = FST.re("$^rewrite((kaa\^aa?):(kvv\^), longest = True, leftmost = True)", fsts)


        #uu (SetB [3S-Sub/3S-inanimate-Obj])
        rule4 = FST.re("$^rewrite((uu):(uw) / _ \^ [eou])", fsts)
        rule5 = FST.re("$^rewrite((uu\^vv?):(uwa\^), longest = True, leftmost = True)", fsts)
        rule6 = FST.re("$^rewrite(a:'' / uu\^ _ )", fsts)
        #rule7 --> Add later

        #Remove any double morpheme boundary markers (^^) as these will interfere
        #with final vowel dropping rules
        cleanup1 = FST.re("$^rewrite(\^:'' / \^ _)", fsts)
        #Remove ?
        cleanup2 = FST.re("$^rewrite(\?:'')", fsts)

        rule8 = FST.re("$^rewrite((ii?|aa?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)
        rule9 = FST.re("$^rewrite((vv?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)


        fsts['Lexicon'] = Lexicon
        fsts['rule1'] = rule1
        fsts['rule2'] = rule2
        fsts['rule2_1'] = rule2_1
        fsts['rule3'] = rule3
        fsts['metathesis1'] = metathesis1
        fsts['metathesis2'] = metathesis2
        fsts['metathesis3'] = metathesis3
        fsts['aspiration'] = aspiration
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
        fsts['cleanup2'] = cleanup2
        fsts['rule8'] = rule8
        fsts['rule9'] = rule9
        self.final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $metathesis3 @ $aspiration @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $cleanup2 @ $rule8 @ $rule9", fsts)


    def generate(imput):
        return self.final.generate(input)

    def generate(imput):
        return self.final.analyze(input)
    

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

    

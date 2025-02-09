#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm

import json
import logging
import sys

from morphy_base import morphy_base

class morph_definitions():
    def __init__():
        self.sets_pre = None
        self.transitive = None
        self.subject = None
        self.two_local = None
        self.object_focus = None

class morph_defs_latin():
    def __init__(self):
    
        self.stems = {
            'PresCont': [
                'ᏍᏕᎵᎭ',
                'ᎤᎢᎶᎠ',
                'ᎣᎩᏍᎦ',
                'ᎥᏃᏌᏍᎦ',
                'ᎥᏂᎭ',
                'ᏬᏂᎭ',
                'ᎠᎢ',
                'ᏅᏥᏙᎭ',
                'ᎡᏡᎦ',
                'ᎠᏚᎵᎭ',
                'ᎣᎩᏍᎦ',
            ],
            
            #'setA': [ "ji^",
            #     "iinii^",
            #     "iitii^",
            #     "oostii^",
            #     "oojii^",
            #     "hi^",
            #     "stii^",
            #     "iijii^",
            #     "a^",
            #     "ka^",
            #     "anii^"
            # ],
            # 'setB': [
            #     "aki^",
            #     "kinii^",
            #     "iikii^",
            #     "ookinii^",
            #     "ookii^",
            #     "ja^",
            #     "stii^",
            #     "iijii^",
            #     "uu^",
            #     "uunii^",
            # ],
            # 'animate_3SO': [
            #     "jii^",
            #     "eenii^",
            #     "eetii^",
            #     "oostii^",
            #     "oojii^",
            #     "hii^",
            #     "eestii^",
            #     "eejii^",
            #     "a^",
            #     "ka^",
            #     "anii^"]
        }

        #Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)
        self.setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ji^"), \
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

        self.setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "aki^"), \
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
        self.animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "jii^"), \
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

        self.subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "aki^"), \
            ("'[3S-Sub/1D-inc-Obj]+'", "kinii^"), \
            ("'[3S-Sub/1P-inc-Obj]+'", "iikii^"), \
            ("'[3S-Sub/1D-ex-Obj]+'", "ookinii^"), \
            ("'[3S-Sub/1P-ex-Obj]+'", "ookii^"), \
            ("'[3S-Sub/2S-Obj]+'", "ja^"), \
            ("'[3S-Sub/2D-Obj]+'", "stii^"), \
            ("'[3S-Sub/2P-Obj]+'", "iijii^")]

        self.subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "kvvki^"), \
            ("'[3P-Sub/1D-inc-Obj]+'", "keekinii^"), \
            ("'[3P-Sub/1P-inc-Obj]+'", "keekii^"), \
            ("'[3P-Sub/1D-ex-Obj]+'", "kookinii^"), \
            ("'[3P-Sub/1P-ex-Obj]+'", "kookii^"), \
            ("'[3P-Sub/2S-Obj]+'", "keeja^"), \
            ("'[3P-Sub/2D-Obj]+'", "keestii^"), \
            ("'[3P-Sub/2P-Obj]+'", "keejii^")]

        self.two_local = [("'[2S-Sub/1S-Obj]+'", "ski^"), \
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

        self.object_focus = [("'[1S-inc-Obj]+'", "vvki^"), \
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

        self.setA_tups = [(a, "SetA_Verbs") for a in self.setA_pre]
        self.setB_tups = [(b, "SetB_Verbs") for b in self.setB_pre]
        self.animate_obj_tups = [(c, "Transitive_Verbs") for c in self.animate_3SO]
        self.subj_3S_tups = [(d, "Transitive_Verbs") for d in self.subject_3S]
        self.subj_3P_tups = [(e, "Transitive_Verbs") for e in self.subject_3P]
        self.two_loc_tups = [(f, "Transitive_Verbs") for f in self.two_local]
        self.ob_foc_tups = [(g, "Transitive_Verbs") for g in self.object_focus]


        self.fin_person = (self.setA_tups +
                           self.setB_tups +
                           self.animate_obj_tups +
                           self.subj_3S_tups +
                           self.subj_3P_tups + self.two_loc_tups + self.ob_foc_tups)

        self.Grammar = {}
        self.Grammar["S"] = [("", "Prefix1")]

        self.Grammar["Prefix1"] = [("", "Prefix2"), \
                      (("'[IRR]+'", "yi^"), "Prefix2"), \
                      (("'[REL]+'", "j?i^"), "Prefix2"), \
                      (("'[NGI]+'", "?jii^"), "Prefix2")]

        self.Grammar["Prefix2"] = [("", "Prefix3"), \
                      (("'[TRN]+'", "wi^"), "Prefix3")]

        self.Grammar["Prefix3"] = [("", "Prefix7"), \
                      (("'[PRT]+'", "ni^"), "Prefix7")]

        self.Grammar["Prefix7"] = [("", "PersonPrefixes"), \
                      (("'[NGT]+'", "kaa^"), "PersonPrefixes")]


        self.Grammar["PersonPrefixes"] = self.fin_person

        self.Grammar["SetA_Verbs"] = [("", "Intrans_SetA"), ("", "Trans_SetA")]
        self.Grammar["SetB_Verbs"] = [("", "Intrans_SetB"), ("", "Trans_SetB")]
        self.Grammar["Transitive_Verbs"] = [("", "Trans_SetA"), ("", "Trans_SetB")]


        self.Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "wooniha"), "#"), \
                           (("'ᏬᏂᎭ''+[V]''+[Incompletive]'", "woonisk"), "Habitual"), \
                           (("'ᏬᏂᎭ''+[V]''+[Immediate]'", "woonihi"), "#"), \
                           (("'ᎠᎢ''+[V]''+[PresCont]'", "aaʔi"), "#"), \
                           (("'ᎠᎢ''+[V]''+[Incompletive]'", "aaɁis"), "Habitual"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "nvvjiitooha"), "#"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Incompletive]'", "nvvjiitooh"), "Habitual"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Immediate]'", "nvvjiita"), "#")]

        self.Grammar["Intrans_SetB"] = [(("'ᏬᏂᎭ''+[V]''+[Completive]'", "woonis"), "Stem2and4Final"), \
                           (("'ᏬᏂᎭ''+[V]''+[DeVerbalNoun]'", "woonihist"), "Stem5Final"), \
                           (("'ᎠᎢ''+[V]''+[Completive]'", "aaɁis"), "Stem2and4Final"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "nvvjiitool"), "Stem2and4Final"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[DeVerbalNoun]'", "nvvjiitaast"), "Stem5Final"), \
                           (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "eehluuhka"), "#"), \
                           (("'ᎡᏡᎦ''+[V]''+[Incompletive]'", "eehluuhk"), "Habitual"), \
                           (("'ᎡᏡᎦ''+[V]''+[Immediate]'", "eehluhvvka"), "#"), \
                           (("'ᎡᏡᎦ''+[V]''+[Completive]'", "eehluhn"), "Stem2and4Final"), \
                           (("'ᎡᏡᎦ''+[V]''+[DeVerbalNoun]'", "eehluhvst"), "Stem5Final")]

        self.Grammar["Trans_SetA"] = [(("'ᏍᏕᎵᎭ''+[V]''+[PresCont]'", "steeliha"), "#"), \
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
                         (("'ᎥᏂᎭ''+[V]''+[Immediate]'", "vvnika"), "#")]

        self.Grammar["Trans_SetB"] = [(("'ᏍᏕᎵᎭ''+[V]''+[Completive]'", "steelvvh"), "Stem2and4Final"), \
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
                         (("'ᎠᏚᎵᎭ''+[V]''+[DeVerbalNoun]'", "atuuhlt"), "Stem5Final")]

        self.Grammar["Habitual"] = [(("'+[Habitual]'", "^oʔi"), "#"), \
                                    ("", "Stem2and4Final")]
        self.Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^vvʔi"), "#"), \
                                          (("'+[NonExpPast]'", "^eʔi"), "#"), \
                                          (("'+[AbsFut]'", "^éesti"), "#")]
        self.Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^i"), "#"), \
                                      (("'+[NomAbility]'", "^ííʔi"), "#")]



        self.Lexicon = FST.rlg(self.Grammar, "S")
        self.Lexicon = self.Lexicon.epsilon_remove().determinize().minimize()

        self.fsts = {}
        self.fsts['V'] = FST.re("[aeiouv]")         # Vowels

        #Numbered Rules relate to person markers.
        #Rules 8 and 9 are for vowel dropping
        #NGT rules relate to the negative time prefix
        #Cleanup rules remove morpheme boundary markers (^)
        #Rules must be applied in the order below in order to work properly.


        self.rule1 = FST.re("$^rewrite((ji):k / _ \^ $V)", self.fsts)

        self.rule2 = FST.re("$^rewrite('':y / [#|\^](j|h|iisk)ii _ \^ $V)", self.fsts)

        #kvv-, iistvv-, iijvv
        self.rule2_1 = FST.re("$^rewrite('':y / (k|t|j)vv _ \^ $V)", self.fsts)

        self.rule3 = FST.re("$^rewrite((ki):(kw) / _ \^ $V)", self.fsts)

        #Metathesis with /h/ Yi^h -> hy^
        self.metathesis1 = FST.re("$^rewrite((yi\^h):(hy\^))", self.fsts)
        self.metathesis2 = FST.re("$^rewrite((wi\^h):(hw\^))", self.fsts)
        self.metathesis3 = FST.re("$^rewrite((ni\^h):(hn\^))", self.fsts)

        #aspiration
        self.aspiration = FST.re("$^rewrite((j\?i\^h):(ch\^))", self.fsts)

        #Translocative Prefix (we, [TRN]+) --> yi -> yu and ji -> ju before (wi-)
        self.trn = FST.re("$^rewrite(i:u / (y|j\?) _ \^wi)", self.fsts)


        #Negative Time Prefix (kaa, [NGT]+) rules

        #kaa + uu = kvv^wa 
        self.ngt1 = FST.re("$^rewrite((kaa\^uu):(kvv\^wa))", self.fsts)

        #kvv^wa^ + v = kvv^wa^
        self.ngt2 = FST.re("$^rewrite((vv?):'' / kvv\^wa\^ _ , longest = True, leftmost = True)", self.fsts)

        #Kaa + aji = k^eji
        self.ngt3 = FST.re("$^rewrite(a:e / kaa\^ _ (ji|k)\^ )", self.fsts)

        #Kaa + [eiov] = kaay^ + [eiov]
        self.ngt4 = FST.re("$^rewrite('':y / kaa _ \^ [eiov])", self.fsts)

        #Kaa + a = kvv^
        #ngt4 = FST.re("$^rewrite((aa\^aa?):(vv) / [#|\^]k _ , longest = True, leftmost = True)", self.fsts)
        self.ngt5 = FST.re("$^rewrite((kaa\^aa?):(kvv\^), longest = True, leftmost = True)", self.fsts)


        #uu (SetB [3S-Sub/3S-inanimate-Obj])
        self.rule4 = FST.re("$^rewrite((uu):(uw) / _ \^ [eou])", self.fsts)
        self.rule5 = FST.re("$^rewrite((uu\^vv?):(uwa\^), longest = True, leftmost = True)", self.fsts)
        self.rule6 = FST.re("$^rewrite(a:'' / uu\^ _ )", self.fsts)
        #rule7 --> Add later

        #Remove any double morpheme boundary markers (^^) as these will interfere
        #with final vowel dropping rules
        self.cleanup1 = FST.re("$^rewrite(\^:'' / \^ _)", self.fsts)

        #Remove ?
        self.cleanup2 = FST.re("$^rewrite(\?:'')", self.fsts)
        
        self.rule8 = FST.re("$^rewrite((ii?|aa?):'' / _ \^ $V, longest = True, leftmost = True)", self.fsts)
        self.rule9 = FST.re("$^rewrite((vv?):'' / _ \^ $V, longest = True, leftmost = True)", self.fsts)
        self.rules =[
            self.rule1,
            self.rule2,
            self.rule2_1,
            self.rule3,
            self.rule4,
            self.rule5,
            self.rule6,
            self.rule8,
            self.rule9
        ]
         

        #Cleaned = FST.re("$^rewrite(\^:'')")

        self.fsts['Lexicon'] = self.Lexicon
        self.fsts['rule1'] = self.rule1
        self.fsts['rule2'] = self.rule2
        self.fsts['rule2_1'] = self.rule2_1
        self.fsts['rule3'] = self.rule3
        self.fsts['metathesis1'] = self.metathesis1
        self.fsts['metathesis2'] = self.metathesis2
        self.fsts['metathesis3'] = self.metathesis3
        self.fsts['aspiration'] = self.aspiration
        self.fsts['trn'] = self.trn
        self.fsts['ngt1'] = self.ngt1
        self.fsts['ngt2'] = self.ngt2
        self.fsts['ngt3'] = self.ngt3
        self.fsts['ngt4'] = self.ngt4
        self.fsts['ngt5'] = self.ngt5
        self.fsts['rule4'] = self.rule4
        self.fsts['rule5'] = self.rule5
        self.fsts['rule6'] = self.rule6
        self.fsts['cleanup1'] = self.cleanup1
        self.fsts['cleanup2'] = self.cleanup2
        self.fsts['rule8'] = self.rule8
        self.fsts['rule9'] = self.rule9
        self.final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $metathesis3 @ $aspiration @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $cleanup2 @ $rule8 @ $rule9", self.fsts)


class gloss():
    def __init__(self):

        self.prefix = [
            'IRR',
            'NGI',
            'NGT',
            'PRT',
            'REL',
            'TRN',
        ]

        self.part1 = [
            '1D-Sub',
            '1D-ex-Obj',
            '1D-ex-Sub',
            '1D-inc-Obj',
            '1D-inc-Sub',
            '1P-Sub',
            '1P-ex-Obj',
            '1P-ex-Sub',
            '1P-inc-Obj',
            '1P-inc-Sub',
            '1S-Sub',
            '1S-inc-Obj',
            '1S-inc-Sub',
            '2D-Obj',
            '2D-Sub',
            '2P-Obj',
            '2P-Sub',
            '2S-Obj',
            '2S-Sub',
            '3P-Obj',
            '3P-Sub',
            '3S-Obj',
            '3S-Sub',
        ]

        self.part2 = [
            '1D-Obj',
            '1D-ex-Obj',
            '1D-inc-Obj',
            '1P-Obj',
            '1P-ex-Obj',
            '1P-inc-Obj',
            '1S-Obj',
            '1S-inc-Obj',
            '2D-Obj',
            '2P-Obj',
            '2S-Obj',
            '3S-animate-Obj',
            '3S-inanimate-Obj'
        ]
        
        self.after_verb = [
            'Completive',
            'DeVerbalNoun',
            'Immediate',
            'Incompletive',
            'PresCont'
        ]

        self.stem2_and_4final = [
            'AbsFut',
            'ExpPast',
            'NomAbilityOrObligation',
            'NomAbility',
            'NonExpPast',
        ]

        self.prefix = [
            'IRR',
            'NGI',
            'NGT',
            'PRT',
            'REL',
            'TRN',
        ]

        # TODO: add the punctuation needed around each item, e.g., [ and ]
        self.gloss_parts = {
            'prefix': self.prefix,
            'verb1': self.part1,
            'verb2': self.part2,  # '/' before, and insert after verb1
            'stem': ['stem'],
            'V': 'V',
            'after verb2': self.after_verb,
            'stem and final': self.stem2_and_4final,
        }
        self.gloss_ui_type = {
            'prefix': 'checkbox',
            'verb1': 'radio',
            'verb2': 'radio',
            'stem': 'checkbox',
            'V': 'checkbox',
            'after verb2': 'radio',
            'stem and final': 'radio',
        }
        self.gloss_include_none = {
            'prefix': False,
            'verb1': False,
            'verb2': False,
            'stem': False,
            'V': False,
            'after verb2': True,
            'stem and final': True,
        }
        self.gloss_visible = {
            'prefix': True,
            'verb1': True,
            'verb2': True,
            'stem': False,
            'V': False,
            'after verb2': True,
            'stem and final': True,
        }
        

class cherokee_morphy(morphy_base):
    def __init__(self):
        # And create another one with syllabary
        latin_defs = morph_defs_latin()

        defs = latin_defs
        self.lang_name = 'ᏣᎳᎩ'
        self.lang_code = 'chr'
        self.Grammar = defs.Grammar
        self.fsts = defs.fsts
        self.final = defs.final
        self.rules = defs.rules
        self.lexicon = defs.Lexicon

        # The gloss symbols for this morphologizer
        self.gloss = gloss()

    def generate(self, text):
        result = list(self.final.generate(text))
        if not result:
            result = "empty"
        return result

    def parse(self, text):
        result = list(self.final.analyze(text))
        if not result:
            result = "empty"

        return result

    def paradigm(self, text):
        # Paradigm(lexicon)
        logging.debug('Paradigm called!')
        result = Paradigm(self.lexicon, text)
        print('PARADIGM result = %s' % len(result.para))
        
        return result.para

    def test(self):
        test_results = 'TEST'
        return test_results



def main():
    morph_cher = cherokee_morphy()
    morph_cher.paradigm('.*')
#    morph_latn = morph_chr_latin()


if __name__ == '__main__':
    main()
    

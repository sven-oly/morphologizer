#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys


# Basis of both syllabary and latin versions
class morph_chr_base():
    def __init__(self):
        self.stems = {}

        self.Grammar = {}

        self.fsts = {}

        # This is not present in morph_chr_syllabary (???)
        self.metathesis3 = None

        self.aspiration = None
        self.aspiration1 = None
        self.aspiration2 = None

        return

    def common_setup(self):
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

    def setup_common_grammar(self):
        self.Grammar["PersonPrefixes"] = self.fin_person

        self.Grammar["SetA_Verbs"] = [("", "Intrans_SetA"), ("", "Trans_SetA")]
        self.Grammar["SetB_Verbs"] = [("", "Intrans_SetB"), ("", "Trans_SetB")]
        self.Grammar["Transitive_Verbs"] = [("", "Trans_SetA"), ("", "Trans_SetB")]

    def finish_setup(self):
        # Create rule list for outside use
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

        # Set up all the fields of the fsts.
        self.fsts['Lexicon'] = self.Lexicon
        self.fsts['rule1'] = self.rule1
        self.fsts['rule2'] = self.rule2
        self.fsts['rule2_1'] = self.rule2_1
        self.fsts['rule3'] = self.rule3
        self.fsts['metathesis1'] = self.metathesis1
        self.fsts['metathesis2'] = self.metathesis2
        self.fsts['metathesis3'] = self.metathesis3
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


# based on Cherokee Syllabary
class morph_chr_syllabary(morph_chr_base):
    def __init__(self):
        super().__init__()

        self.Grammar = {}
        self.fsts = {}

        self.stems = {
            'setA': [
                "Ꮵ^",
                "Ꭲnii^",
                "Ꭲtii^",
                "ᎣᏍtii^",
                "Ꭳjii^",
                "hi^",
                "Ꮝtii^",
                "Ꭲjii^",
                "a^",
                "ka^",
                "Ꭰnii",
            ],
            'setB': [
                "ᎠᎩ^",
                "Ꭹnii^",
                "Ꭲkii^",
                "ᎣᎩnii^",
                "Ꭳkii^",
                "ja^",
                "Ꮝtii^",
                "Ꭲjii^",
                "Ꭴ^",
                "Ꭴnii",
            ],
            'animate_3SO': [
                #Transitive Verbs Only
                "Ꮵi^",
                "Ꭱnii^",
                "Ꭱtii^",
                "ᎣᏍtii^",
                "Ꭳjii^",
                "Ꭿi^",
                "ᎡᏍtii^",
                "Ꭱjii^",
                "a^",
                "ka^",
                "Ꭰnii",
                ]
            }

        #Person Prefixes

        #Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)


        self.setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "Ꮵ^"), \
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


        self.setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ᎠᎩ^"), \
            ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "Ꭹnii^"), \
            ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "Ꭲkii^"), \
            ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ᎣᎩnii^"), \
            ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "Ꭳkii^"), \
            ("'[2S-Sub/3S-inanimate-Obj]+'", "ja^"), \
            ("'[2D-Sub/3S-inanimate-Obj]+'", "Ꮝtii^"), \
            ("'[2P-Sub/3S-inanimate-Obj]+'", "Ꭲjii^"), \
            ("'[3S-Sub/3S-inanimate-Obj]+'", "Ꭴ^"), \
            ("'[3P-Sub/3S-inanimate-Obj]+'", "Ꭴnii^")]

        #Transitive Verbs Only

        self.animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "Ꮵi^"), \
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


        self.subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "ᎠᎩ^"), \
                           ("'[3S-Sub/1D-inc-Obj]+'", "Ꭹnii^"), \
                           ("'[3S-Sub/1P-inc-Obj]+'", "Ꭲkii^"), \
                           ("'[3S-Sub/1D-ex-Obj]+'", "ᎣᎩnii^"), \
                           ("'[3S-Sub/1P-ex-Obj]+'", "Ꭳkii^"), \
                           ("'[3S-Sub/2S-Obj]+'", "ja^"), \
                           ("'[3S-Sub/2D-Obj]+'", "Ꮝtii^"), \
                           ("'[3S-Sub/2P-Obj]+'", "Ꭲjii^")]
        
        self.subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "ᎬᎩ^"), \
                           ("'[3P-Sub/1D-inc-Obj]+'", "ᎨᎩnii^"), \
                           ("'[3P-Sub/1P-inc-Obj]+'", "Ꭸkii^"), \
                           ("'[3P-Sub/1D-ex-Obj]+'", "ᎪᎩnii^"), \
                           ("'[3P-Sub/1P-ex-Obj]+'", "Ꭺkii^"), \
                           ("'[3P-Sub/2S-Obj]+'", "Ꭸja^"), \
                           ("'[3P-Sub/2D-Obj]+'", "ᎨᏍtii^"), \
                           ("'[3P-Sub/2P-Obj]+'", "Ꭸjii^")]


        self.two_local = [("'[2S-Sub/1S-Obj]+'", "ᏍᎩ^"), \
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
    
        self.object_focus = [("'[1S-inc-Obj]+'", "ᎥᎩ^"), \
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

        self.common_setup()
        
        self.setup_Grammar()

        self.Lexicon = FST.rlg(self.Grammar, "S")
        self.Lexicon = self.Lexicon.epsilon_remove().determinize().minimize()

        self.fsts['V'] = FST.re("[aeiouvᎠᎡᎢᎣᎤᎥ]")         # Vowels

        self.rule1 = FST.re("$^rewrite(Ꮵ:k / _ \^ $V)", self.fsts)
        #This stays the same
        #Results in k^vowel (aeouv - verb stems don't start with /i/) needing to be rewritten

        self.rule2 = FST.re("$^rewrite(i:y / [#|\^](Ꮵ|Ꭿ|ᎢᏍᎩ) _ \^ $V)", self.fsts)
        #This becomes i-> in front of ji/hi and before vowel (assuming we write these endigns as (hi)i^)
        #Results in y^vowel needs to be rewritten in syllabary or stray i^ that needs to be removed

        self.rule2_1 = FST.re("$^rewrite('':y / (Ꭼ|Ꮫ|Ꮸ) _ \^ $V)", self.fsts)

        #Write rule to remove stray [i] right here ... no this could be problematic, do it later.

        self.rule3 = FST.re("$^rewrite(Ꭹ:(kw) / _ \^ $V)", self.fsts)
        #change syllabary ki to transcription kw-
        #results in kw^vowel needs to be rewritten

        #Metathesis with /h/ Yi^h -> hy^
        #metathesis1 = FST.re("$^rewrite((yi\^h):(y\^))", self.fsts)

        self.metathesis1 = FST.re("$^rewrite((i\^h):(\^) / (y|w|n) _ )", self.fsts)


        #yi^HIy = HYIy^
        self.metathesis1.is2 = FST.re("$^rewrite(Ꭿ:'' / (y|w|n)i\^ _ )", self.fsts)
        self.metathesis2 = FST.re("$^rewrite(Ꭿ:'' / (y|w|n)i\^ _ )", self.fsts)

        #aspiration
        self.aspiration1 = FST.re("$^rewrite((ji\^h):(j\^))", self.fsts)
        self.aspiration2 = FST.re("$^rewrite((ji\^Ꭿ):(ji\^))", self.fsts)

        #Translocative Prefix (we, [TRN]+) --> yi -> yu and ji -> ju before (wi-)
        self.trn = FST.re("$^rewrite(i:u / (y|j) _ \^wi)", self.fsts)

        #NGT Rules
        #kaa + uu = kvv^wa 
        self.ngt1 = FST.re("$^rewrite((kaa\^Ꭴ):(Ꭼ\^wa))", self.fsts)

        #kvv^wa^ + v = kvv^wa^
        self.ngt2 = FST.re("$^rewrite(Ꭵ:'' / Ꭼ\^wa\^ _ )", self.fsts)

        #Kaa + aji (ᎠᏥ^) = k^eji
        self.ngt3 = FST.re("$^rewrite(Ꭰ:Ꭱ / kaa\^ _ (Ꮵ|k)\^ )", self.fsts)

        #Kaa + [eiov] = kaay^ + [eiov]
        self.ngt4 = FST.re("$^rewrite((kaa):(Ꭶy) / _ \^ [eiovᎡᎢᎣᎥ])", self.fsts)

        #Kaa + a = kvv^
        self.ngt5 = FST.re("$^rewrite((kaa\^(aa?|Ꭰ)):(kvv\^), longest = True, leftmost = True)", self.fsts)

        #uu (SetB [3S-Sub/3S-inanimate-Obj])
        self.rule4 = FST.re("$^rewrite('':w / Ꭴ _ \^ [eouᎡᎣᎤ])", self.fsts)
        #Add roman 'w' after syllabary uu
        #results in w^vowel needs to be rewritten

        self.rule5 = FST.re("$^rewrite((Ꭴ\^Ꭵ):(ᎤᏩ\^))", self.fsts)
        #Syllabary to syllabary

        self.rule6 = FST.re("$^rewrite(Ꭰ:'' / Ꭴ\^ _ )", self.fsts)
        #uu will be in syllabary, a will not

        #rule7 --> Add later
        self.cleanup1 = FST.re("$^rewrite(\^:'' / \^ _)", self.fsts)

        self.rule8 = FST.re("$^rewrite((aa?|ii?):'' / _ \^ $V, longest = True, leftmost = True)", self.fsts)
        self.rule9 = FST.re("$^rewrite((vv?):'' / _ \^ $V, longest = True, leftmost = True)", self.fsts)
        #Results in various consonant^vowel need to be rewritten -> ntjkh
        #try something like k\^?a\^? -> ka (optional morpheme boundaries on either side of 'a' shoooould allow for both ka^consonant and k^a|consonant to be rewritten as ka character)
        #orrrr we could remove the morpheme markers first and then do this

        #Final Suffixes have following pairs:
        #k^vowel (will be take care of with Rule 1)
        #h^vowel (will be taken care of with Rule 8)
        #t_i (will be taken care of with rule 8)
        #Completive can end in a few different consonants, make this all work with rule 8

        #When there is consonant initial verb stem, no vowels change.
        #But we will need to rewrite from transcription to syllabary here for some prefixes

        #Then we'll need to rewrite remaining transcription into syllabary
        #Person markings that attached to a consonant initial stem
        #Person markings that attached to a vowel initial stem
        #Any stray vowels, h's, or glottal stops

        self.cleanup2 = FST.re("$^rewrite(\^:'')")
        #kw -> vowel

        self.fsts['kw_a'] = FST.re("$^rewrite((kwᎠ|kwaa?):Ꮖ, longest = True, leftmost = True)", self.fsts)
        self.fsts['kw_e'] = FST.re("$^rewrite((kwᎡ|kwee?):Ꮗ, longest = True, leftmost = True)", self.fsts)
        self.fsts['kw_i'] = FST.re("$^rewrite((kwᎢ|kwii?):Ꮘ, longest = True, leftmost = True)", self.fsts)
        self.fsts['kw_o'] = FST.re("$^rewrite((kwᎣ|kwoo?):Ꮙ, longest = True, leftmost = True)", self.fsts)
        self.fsts['kw_u'] = FST.re("$^rewrite((kwᎤ|kwuu?):Ꮚ, longest = True, leftmost = True)", self.fsts)
        self.fsts['kw_v'] = FST.re("$^rewrite((kwᎥ|kwvv?):Ꮛ, longest = True, leftmost = True)", self.fsts)

        #k -> vowel
        self.fsts['k_a'] = FST.re("$^rewrite((kᎠ|kaa?):Ꭶ, longest = True, leftmost = True)", self.fsts)
        self.fsts['k_e'] = FST.re("$^rewrite((kᎡ|kee?):Ꭸ, longest = True, leftmost = True)", self.fsts)
        self.fsts['k_i'] = FST.re("$^rewrite((kᎢ|kii?):Ꭹ, longest = True, leftmost = True)", self.fsts)
        self.fsts['k_o'] = FST.re("$^rewrite((kᎣ|koo?):Ꭺ, longest = True, leftmost = True)", self.fsts)
        self.fsts['k_u'] = FST.re("$^rewrite((kᎤ|kuu?):Ꭻ, longest = True, leftmost = True)", self.fsts)
        self.fsts['k_v'] = FST.re("$^rewrite((kᎥ|kvv?):Ꭼ, longest = True, leftmost = True)", self.fsts)

        #Cleaned = FST.re("$^rewrite(\^:'')")
        self.fsts['aspiration1'] = self.aspiration1
        self.fsts['aspiration2'] = self.aspiration2
        self.finish_setup()
        self.final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $aspiration1 @$aspiration2 @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $cleanup2 @ $rule8 @ $rule9", self.fsts)


    def setup_Grammar(self):
        self.Grammar["S"] = [("", "Prefix1")]

        self.Grammar["Prefix1"] = [("", "Prefix2"),
                                   (("'[IRR]+'", "yi^"), "Prefix2"),
                                   (("'[REL]+'", "ji^"), "Prefix2"),
                                   (("'[NGI]+'", "jii^"), "Prefix2")]
        
        self.Grammar["Prefix2"] = [("", "Prefix3"),
                      (("'[TRN]+'", "wi^"), "Prefix3")]

        self.Grammar["Prefix3"] = [("", "Prefix7"),
                                   (("'[PRT]+'", "ni^"), "Prefix7")]
    
        self.Grammar["Prefix7"] = [("", "PersonPrefixes"),
                      (("'[NGT]+'", "kaa^"), "PersonPrefixes")]
    
        self.setup_common_grammar()

        self.Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "ᏬᏂᎭ"), "#"), \
                                        (("'ᏬᏂᎭ''+[V]''+[Incompletive]'", "ᏬᏂᏍk"), "Habitual"), \
                                        (("'ᏬᏂᎭ''+[V]''+[Immediate]'", "ᏬᏂᎯ"), "#"), \
                                        (("'ᎠᎢ''+[V]''+[PresCont]'", "ᎠᎢ"), "#"), \
                                        (("'ᎠᎢ''+[V]''+[Incompletive]'", "ᎠᎢᏍ"), "Habitual"), \
                                        (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "ᏅᏥᏙᎭ"), "#"), \
                                        (("'ᏅᏥᏙᎭ''+[V]''+[Incompletive]'", "ᏅᏥᏙh"), "Habitual"), \
                                        (("'ᏅᏥᏙᎭ''+[V]''+[Immediate]'", "ᏅᏥᏓ"), "#")]    
        
        self.Grammar["Intrans_SetB"] = [(("'ᏬᏂᎭ''+[V]''+[Completive]'", "ᏬᏂᏍ"), "Stem2and4Final"), \
                                        (("'ᏬᏂᎭ''+[V]''+[DeVerbalNoun]'", "ᏬᏂᎯᏍt"), "Stem5Final"), \
                                        (("'ᎠᎢ''+[V]''+[Completive]'", "ᎠᎢᏍ"), "Stem2and4Final"), \
                                        (("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "ᏅᏥᏙl"), "Stem2and4Final"), \
                                        (("'ᏅᏥᏙᎭ''+[V]''+[DeVerbalNoun]'", "ᏅᏥᏓᏍt"), "Stem5Final"), \
                                        (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "ᎡᏡᎦ"), "#"), \
                                        (("'ᎡᏡᎦ''+[V]''+[Incompletive]'", "ᎡᏡk"), "Habitual"), \
                                        (("'ᎡᏡᎦ''+[V]''+[Immediate]'", "ᎡᏡᎲᎦ"), "#"), \
                                        (("'ᎡᏡᎦ''+[V]''+[Completive]'", "ᎡᏡn"), "Stem2and4Final"), \
                                        (("'ᎡᏡᎦ''+[V]''+[DeVerbalNoun]'", "ᎡᏡᎲᏍt"), "Stem5Final")]

        self.Grammar["Trans_SetA"] = [(("'ᏍᏕᎵᎭ''+[V]''+[PresCont]'", "ᏍᏕᎵᎭ"), "#"), \
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
                                      (("'ᎥᏂᎭ''+[V]''+[Immediate]'", "ᎥᏂᎦ"), "#")]

        self.Grammar["Trans_SetB"] = [(("'ᏍᏕᎵᎭ''+[V]''+[Completive]'", "ᏍᏕᎸh"), "Stem2and4Final"), \
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
                                      (("'ᎠᏚᎵᎭ''+[V]''+[DeVerbalNoun]'", "ᎠᏚᎸt"), "Stem5Final")]

        #Grammar["PresCont"] = [(("'+[V]''+[PresCont]'", ""), "#")]
        #Grammar["Incomp"] = [(("'+[V]''+[Incompletive]'", ""), "Habitual")]
        #Grammar["Immediate"] = [(("'+[V]''+[Immediate]'", ""), "#")]
        #Grammar["Comp"] = [(("'+[V]''+[Completive]'", ""), "Stem2and4Final")]
        #Grammar["DeVerb"] = [(("'+[V]''+[DeVerbalNoun]'", ""), "Stem5Final")]

        #Grammar["Habitual"] = [(("'+[Habitual]'", "^oʔi"), "#"), \
            #                       ("", "Stem2and4Final")]

        self.Grammar["Habitual"] = [(("'+[Habitual]'", "^ᎣᎢ"), "#"), \
                                    ("", "Stem2and4Final")]

    
        #Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^vvʔi"), "#"), \
            #                             (("'+[NonExpPast]'", "^eʔi"), "#"), \
            #                             (("'+[AbsFut]'", "^éesti"), "#")]

        self.Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^ᎥᎢ"), "#"), \
                                          (("'+[NonExpPast]'", "^ᎡᎢ"), "#"), \
                                          (("'+[AbsFut]'", "^ᎡᏍᏗ"), "#")]
        
        #Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^i"), "#"), \
            #                         (("'+[NomAbility]'", "^ííʔi"), "#")]

        self.Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^Ꭲ"), "#"), \
                                      (("'+[NomAbility]'", "^ᎢᎢ"), "#")]

        
# Based on Latin letters
class morph_chr_latin(morph_chr_base):
    def __init__(self):
        super().__init__()
        self.Grammar = {}

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
                'ᎠᏕᎦ',
                'ᎨᏳᎭ',
                'ᎪᏂᏲᎦ',
                'ᎠᏂᎭ',
                'ᏲᎷᎭ',
                'ᎵᏓᏍᏗᎭ',
                'ᏁᎫᏣ',
                'ᎠᏛᏓᏍᏗ',
                'ᏅᏆᎶᎠ',
                'ᏪᏟᎭ',
            ]
        }
        self.stems_translated = {
            'PresCont': [
                ['None', 'None'],
                ['ᏍᏕᎵᎭ', 'to help'],
                ['ᎤᎢᎶᎠ', 'to wash'],
                ['ᎣᎩᏍᎦ', 'to smoke'],
                ['ᎥᏃᏌᏍᎦ', 'to sweep'],
                ['ᎥᏂᎭ', 'to hit'],
                ['ᏬᏂᎭ', 'to speak'],
                ['ᎠᎢ', 'to walk'],
                ['ᏅᏥᏙᎭ', 'to toss about'],
                ['ᎡᏡᎦ', 'to yell, howl, meow'],
                ['ᎠᏚᎵᎭ', 'to want'],
                ['ᎠᏕᎦ', 'to pitch/throw (a ball'],
                ['ᎨᏳᎭ', 'to be possessive of something'],
                ['ᎪᏂᏲᎦ', 'to be late'],
                ['ᎠᏂᎭ', 'to be in bed'],
                ['ᏲᎷᎭ', 'to float'],
                ['ᎵᏓᏍᏗᎭ', 'to make a mistake'],
                ['ᏁᎫᏣ', 'to be mean'],
                ['ᎠᏛᏓᏍᏗ', 'to listen'],
                ['ᏅᏆᎶᎠ', 'to hammer something'],
                ['ᏪᏟᎭ', 'to joke/tease'],
            ]
        }
        self.notstems = {
            'setA': [
                "ji^",
                "iinii^",
                "iitii^",
                "oostii^",
                "oojii^",
                "hi^",
                "stii^",
                "iijii^",
                "a^",
                "ka^",
                "anii^"
            ],
            'setB': [
                "aki^",
                "kinii^",
                "iikii^",
                "ookinii^",
                "ookii^",
                "ja^",
                "stii^",
                "iijii^",
                "uu^",
                "uunii^",
            ],
            'animate_3SO': [
                "jii^",
                "eenii^",
                "eetii^",
                "oostii^",
                "oojii^",
                "hii^",
                "eestii^",
                "eejii^",
                "a^",
                "ka^",
                "anii^"]
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

        # Steps in setup 
        self.common_setup()

        self.setup_Grammar()
        
        self.Lexicon = FST.rlg(self.Grammar, "S")
        self.Lexicon = self.Lexicon.epsilon_remove().determinize().minimize()

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

        self.fsts['aspiration'] = self.aspiration

        self.finish_setup()
        self.final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $metathesis3 @ $aspiration @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $cleanup2 @ $rule8 @ $rule9", self.fsts)


    def setup_Grammar(self):
        
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


        self.setup_common_grammar()


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


def main(argv):
    morph_cher = morph_chr_syllabary()
    morph_latn = morph_chr_latin()


if __name__ == '__main__':
  main(sys.argv)

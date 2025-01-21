#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys

from morphy_base import morphy_base

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

Grammar = {}
Grammar["S"] = [("", "Prefix1")]

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


Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "wooniha"), "#"), \
                           (("'ᏬᏂᎭ''+[V]''+[Incompletive]'", "woonisk"), "Habitual"), \
                           (("'ᏬᏂᎭ''+[V]''+[Immediate]'", "woonihi"), "#"), \
                           (("'ᎠᎢ''+[V]''+[PresCont]'", "aaʔi"), "#"), \
                           (("'ᎠᎢ''+[V]''+[Incompletive]'", "aaɁis"), "Habitual"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "nvvjiitooha"), "#"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Incompletive]'", "nvvjiitooh"), "Habitual"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Immediate]'", "nvvjiita"), "#")]

Grammar["Intrans_SetB"] = [(("'ᏬᏂᎭ''+[V]''+[Completive]'", "woonis"), "Stem2and4Final"), \
                           (("'ᏬᏂᎭ''+[V]''+[DeVerbalNoun]'", "woonihist"), "Stem5Final"), \
                           (("'ᎠᎢ''+[V]''+[Completive]'", "aaɁis"), "Stem2and4Final"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "nvvjiitool"), "Stem2and4Final"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[DeVerbalNoun]'", "nvvjiitaast"), "Stem5Final"), \
                           (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "eehluuhka"), "#"), \
                           (("'ᎡᏡᎦ''+[V]''+[Incompletive]'", "eehluuhk"), "Habitual"), \
                           (("'ᎡᏡᎦ''+[V]''+[Immediate]'", "eehluhvvka"), "#"), \
                           (("'ᎡᏡᎦ''+[V]''+[Completive]'", "eehluhn"), "Stem2and4Final"), \
                           (("'ᎡᏡᎦ''+[V]''+[DeVerbalNoun]'", "eehluhvst"), "Stem5Final")]

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
                         (("'ᎥᏂᎭ''+[V]''+[Immediate]'", "vvnika"), "#")]

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
                         (("'ᎠᏚᎵᎭ''+[V]''+[DeVerbalNoun]'", "atuuhlt"), "Stem5Final")]

Grammar["Habitual"] = [(("'+[Habitual]'", "^oʔi"), "#"), \
                       ("", "Stem2and4Final")]
Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^vvʔi"), "#"), \
                             (("'+[NonExpPast]'", "^eʔi"), "#"), \
                             (("'+[AbsFut]'", "^éesti"), "#")]
Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^i"), "#"), \
                         (("'+[NomAbility]'", "^ííʔi"), "#")]



Lexicon = FST.rlg(Grammar, "S")
Lexicon = Lexicon.epsilon_remove().determinize().minimize()

fsts = {}
fsts['V'] = FST.re("[aeiouv]")         # Vowels

#Numbered Rules relate to person markers.
#Rules 8 and 9 are for vowel dropping
#NGT rules relate to the negative time prefix
#Cleanup rules remove morpheme boundary markers (^)
#Rules must be applied in the order below in order to work properly.

rule1 = FST.re("$^rewrite((ji):k / _ \^ $V)", fsts)

rule2 = FST.re("$^rewrite('':y / [#|\^](j|h|iisk)ii _ \^ $V)", fsts)

#kvv-, iistvv-, iijvv
rule2_1 = FST.re("$^rewrite('':y / (k|t|j)vv _ \^ $V)", fsts)

rule3 = FST.re("$^rewrite((ki):(kw) / _ \^ $V)", fsts)

#Metathesis with /h/ Yi^h -> hy^
metathesis1 = FST.re("$^rewrite((yi\^h):(hy\^))", fsts)
metathesis2 = FST.re("$^rewrite((wi\^h):(hw\^))", fsts)
metathesis3 = FST.re("$^rewrite((ni\^h):(hn\^))", fsts)

#aspiration
aspiration = FST.re("$^rewrite((j\?i\^h):(ch\^))", fsts)

#Translocative Prefix (we, [TRN]+) --> yi -> yu and ji -> ju before (wi-)
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
#ngt4 = FST.re("$^rewrite((aa\^aa?):(vv) / [#|\^]k _ , longest = True, leftmost = True)", fsts)
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

#Cleaned = FST.re("$^rewrite(\^:'')")

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
final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $metathesis1 @ $metathesis2 @ $metathesis3 @ $aspiration @ $trn @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $cleanup2 @ $rule8 @ $rule9", fsts)


class cherokee_morphy(morphy_base):
    def __init__(self):
        self.lang_name = 'ᏣᎳᎩ'
        self.lang_code = 'chr'
        self.Grammar = Grammar
        self.fsts = fsts
        self.final = final
        self.rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule8, rule9]

        

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

    def test(self):
        test_results = 'TEST'
        return test_results


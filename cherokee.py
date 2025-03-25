#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys

function = sys.argv[1]
cherokee = sys.argv[2]

#Person Prefixes

#Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)
setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ji^"), \
            ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "iinii^"), ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iitii^"), \
            ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "oostii^"), ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "oojii^"), \
            ("'[2S-Sub/3S-inanimate-Obj]+'", "hi^"), ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
            ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), ("'[3S-Sub/3S-inanimate-Obj]+'", "a^"), \
            ("'[3S-Sub/3S-inanimate-Obj]+'", "ka^"), ("'[3P-Sub/3S-inanimate-Obj]+'", "anii^")]

setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "aki^"), \
            ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "kinii^"), ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iikii^"), \
            ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ookinii^"), ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "ookii^"), \
            ("'[2S-Sub/3S-inanimate-Obj]+'", "ja^"), ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
            ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), ("'[3S-Sub/3S-inanimate-Obj]+'", "uu^"), \
            ("'[3P-Sub/3S-inanimate-Obj]+'", "uunii^")]

#Transitive Verbs Only
animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "jii^"), \
            ("'[1D-inc-Sub/3S-animate-Obj]+'", "eenii^"), ("'[1P-inc-Sub/3S-animate-Obj]+'", "eetii^"), \
            ("'[1D-ex-Sub/3S-animate-Obj]+'", "oostii^"), ("'[1P-ex-Sub/3S-animate-Obj]+'", "oojii^"), \
            ("'[2S-Sub/3S-animate-Obj]+'", "hii^"), \
            ("'[2D-Sub/3S-animate-Obj]+'", "eestii^"), ("'[2P-Sub/3S-animate-Obj]+'", "eejii^"), \
            ("'[3S-Sub/3S-animate-Obj]+'", "a^"), ("'[3S-Sub/3S-animate-Obj]+'", "ka^"), \
            ("'[3P-Sub/3S-animate-Obj]+'", "anii^")]

subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "aki^"), \
            ("'[3S-Sub/1D-inc-Obj]+'", "kinii^"), ("'[3S-Sub/1P-inc-Obj]+'", "iikii^"), \
            ("'[3S-Sub/1D-ex-Obj]+'", "ookinii^"), ("'[3S-Sub/1P-ex-Obj]+'", "ookii^"), \
            ("'[3S-Sub/2S-Obj]+'", "ja^"), ("'[3S-Sub/2D-Obj]+'", "stii^"), \
            ("'[3S-Sub/2P-Obj]+'", "iijii^")]

subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "kvvki^"), \
            ("'[3P-Sub/1D-inc-Obj]+'", "keekinii^"), ("'[3P-Sub/1P-inc-Obj]+'", "keekii^"), \
            ("'[3P-Sub/1D-ex-Obj]+'", "kookinii^"), ("'[3P-Sub/1P-ex-Obj]+'", "kookii^"), \
            ("'[3P-Sub/2S-Obj]+'", "keeja^"), ("'[3P-Sub/2D-Obj]+'", "keestii^"), \
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
            ("'[1D-inc-Obj]+'", "eekinii^"), ("'[1P-inc-Obj]+'", "eekii^"), \
            ("'[1D-ex-Obj]+'", "ookinii^"), ("'[1P-ex-Obj]+'", "oojii^"), \
            ("'[2S-Obj]+'", "eeja^"), ("'[2D-Obj]+'", "eestii^"), \
            ("'[2P-Obj]+'", "eejii^"), ("'[3S-Obj]+'", "aji^"), \
            ("'[3P-Obj]+'", "keejii^"), ("'[3P-Obj]+'", "keek^")]


setA_tups = [(a, "SetA_Verbs") for a in setA_pre]
setB_tups = [(b, "SetB_Verbs") for b in setB_pre]
animate_obj_tups = [(c, "Transitive_Verbs") for c in animate_3SO]
subj_3S_tups = [(d, "Transitive_Verbs") for d in subject_3S]
subj_3P_tups = [(e, "Transitive_Verbs") for e in subject_3P]
two_loc_tups = [(f, "Transitive_Verbs") for f in two_local]
ob_foc_tups = [(g, "Transitive_Verbs") for g in object_focus]



fin_person = setA_tups + setB_tups + animate_obj_tups + subj_3S_tups + subj_3P_tups + two_loc_tups + ob_foc_tups

Grammar = {}
Grammar["S"] = [("", "PersonPrefixes")]
Grammar["PersonPrefixes"] = fin_person

Grammar["SetA_Verbs"] = [("", "Intrans_SetA"), ("", "Trans_SetA")]
Grammar["SetB_Verbs"] = [("", "Intrans_SetB"), ("", "Trans_SetB")]
Grammar["Transitive_Verbs"] = [("", "Trans_SetA"), ("", "Trans_SetB")]

Grammar["Intrans_SetA"] = [("wooniha", "PresCont"), \
                           ("aaʔi", "PresCont")]

Grammar["Intrans_SetB"] = [("nvjiithl", "Comp"), \
                           ("eeluukiisk", "Incomp")]

Grammar["Trans_SetA"] = [("steeliha", "PresCont"), \
                         ("steeliisk", "Incomp"), \
                         ("steela", "Immediate"), \
                         ("ookiska", "PresCont")]

Grammar["Trans_SetB"] = [("steelvvh", "Comp"), \
                         ("stehlt", "DeVerb"), \
                         ("uuhiiloo", "Comp"), \
                         ("vvnoosah", "Comp"), \
                         ("vhthan", "Comp"), \
                         ("atuuliha", "PresCont")]

Grammar["PresCont"] = [(("'+[V]''+[PresCont]'", ""), "#")]
Grammar["Incomp"] = [(("'+[V]''+[Incompletive]'", ""), "Habitual")]
Grammar["Immediate"] = [(("'+[V]''+[Immediate]'", ""), "#")]
Grammar["Comp"] = [(("'+[V]''+[Completive]'", ""), "Stem2and4Final")]
Grammar["DeVerb"] = [(("'+[V]''+[DeVerbalNoun]'", ""), "Stem5Final")]

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

rule1 = FST.re("$^rewrite((ji):k / _ \^ $V)", fsts)
rule2 = FST.re("$^rewrite('':y / [#|\^][j|h]ii _ \^ $V)", fsts)
rule3 = FST.re("$^rewrite((ki):(kw) / _ \^ $V)", fsts)
rule4 = FST.re("$^rewrite((uu):(uw) / _ \^ [eou])", fsts)
rule5 = FST.re("$^rewrite((uu\^vv?):(uwa\^))", fsts)
rule6 = FST.re("$^rewrite(a:'' / uu\^ _ )", fsts)
#rule7 --> Add later
rule8 = FST.re("$^rewrite((ii?|a):'' / _ \^ $V, longest = True, leftmost = True)", fsts)
#Cleaned = FST.re("$^rewrite(\^:'')")

fsts['Lexicon'] = Lexicon
fsts['rule1'] = rule1
fsts['rule2'] = rule2
fsts['rule3'] = rule3
fsts['rule4'] = rule4
fsts['rule5'] = rule5
fsts['rule6'] = rule6
fsts['rule8'] = rule8
final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule3 @ $rule4 @ $rule5 @ $rule6 @ $rule8", fsts)


print(function, cherokee)

if function == 'generate':
    res = list(final.generate(cherokee))
elif function == 'parse':
    res = list(final.analyze(cherokee))
else:
    print("Arg1 must be either 'generate' or 'parse'")

print(res)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:27:05 2024

@author: vipashabansal
"""
from pyfoma import FST
from pyfoma import Paradigm
import sys

#to get flags to work try from pyfoma import Flags or just import pyfoma
#Actually no it should be working cus imported into FST in code. mess aroudn with it some more instead.

#function = sys.argv[1]
#cherokee = sys.argv[2]

#Person Prefixes

#Set A and B (Intransitive Verbs or Transitive Verbs with a 3S Inanimate Object)

#setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "ji^"), \
#            ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "iinii^"), \
#            ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iitii^"), \
#            ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "oostii^"), \
#            ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "oojii^"), \
#            ("'[2S-Sub/3S-inanimate-Obj]+'", "hi^"), \
#            ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
#            ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), \
#            ("'[3S-Sub/3S-inanimate-Obj]+'", "a^"), \
#            ("'[3S-Sub/3S-inanimate-Obj]+'", "ka^"), \
#            ("'[3P-Sub/3S-inanimate-Obj]+'", "anii^")]

setA_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "Ꮵ^"), \
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

#setB_pre = [("'[1S-inc-Sub/3S-inanimate-Obj]+'", "aki^"), \
#            ("'[1D-inc-Sub/3S-inanimate-Obj]+'", "kinii^"), \
#            ("'[1P-inc-Sub/3S-inanimate-Obj]+'", "iikii^"), \
#            ("'[1D-ex-Sub/3S-inanimate-Obj]+'", "ookinii^"), \
#            ("'[1P-ex-Sub/3S-inanimate-Obj]+'", "ookii^"), \
#            ("'[2S-Sub/3S-inanimate-Obj]+'", "ja^"), \
#            ("'[2D-Sub/3S-inanimate-Obj]+'", "stii^"), \
#            ("'[2P-Sub/3S-inanimate-Obj]+'", "iijii^"), \
#            ("'[3S-Sub/3S-inanimate-Obj]+'", "uu^"), \
#            ("'[3P-Sub/3S-inanimate-Obj]+'", "uunii^")]

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

#Transitive Verbs Only
#animate_3SO = [("'[1S-inc-Sub/3S-animate-Obj]+'", "jii^"), \
#            ("'[1D-inc-Sub/3S-animate-Obj]+'", "eenii^"), \
#            ("'[1P-inc-Sub/3S-animate-Obj]+'", "eetii^"), \
#            ("'[1D-ex-Sub/3S-animate-Obj]+'", "oostii^"), \
#            ("'[1P-ex-Sub/3S-animate-Obj]+'", "oojii^"), \
#            ("'[2S-Sub/3S-animate-Obj]+'", "hii^"), \
#            ("'[2D-Sub/3S-animate-Obj]+'", "eestii^"), \
#            ("'[2P-Sub/3S-animate-Obj]+'", "eejii^"), \
#            ("'[3S-Sub/3S-animate-Obj]+'", "a^"), \
#            ("'[3S-Sub/3S-animate-Obj]+'", "ka^"), \
#            ("'[3P-Sub/3S-animate-Obj]+'", "anii^")]

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


#subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "aki^"), \
#            ("'[3S-Sub/1D-inc-Obj]+'", "kinii^"), \
#            ("'[3S-Sub/1P-inc-Obj]+'", "iikii^"), \
#            ("'[3S-Sub/1D-ex-Obj]+'", "ookinii^"), \
#            ("'[3S-Sub/1P-ex-Obj]+'", "ookii^"), \
#            ("'[3S-Sub/2S-Obj]+'", "ja^"), \
#            ("'[3S-Sub/2D-Obj]+'", "stii^"), \
#            ("'[3S-Sub/2P-Obj]+'", "iijii^")]

subject_3S = [("'[3S-Sub/1S-inc-Obj]+'", "ᎠᎩ^"), \
            ("'[3S-Sub/1D-inc-Obj]+'", "Ꭹnii^"), \
            ("'[3S-Sub/1P-inc-Obj]+'", "Ꭲkii^"), \
            ("'[3S-Sub/1D-ex-Obj]+'", "ᎣᎩnii^"), \
            ("'[3S-Sub/1P-ex-Obj]+'", "Ꭳkii^"), \
            ("'[3S-Sub/2S-Obj]+'", "ja^"), \
            ("'[3S-Sub/2D-Obj]+'", "Ꮝtii^"), \
            ("'[3S-Sub/2P-Obj]+'", "Ꭲjii^")]

#subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "kvvki^"), \
#            ("'[3P-Sub/1D-inc-Obj]+'", "keekinii^"), \
#            ("'[3P-Sub/1P-inc-Obj]+'", "keekii^"), \
#            ("'[3P-Sub/1D-ex-Obj]+'", "kookinii^"), \
#            ("'[3P-Sub/1P-ex-Obj]+'", "kookii^"), \
#            ("'[3P-Sub/2S-Obj]+'", "keeja^"), \
#            ("'[3P-Sub/2D-Obj]+'", "keestii^"), \
#            ("'[3P-Sub/2P-Obj]+'", "keejii^")]

subject_3P = [("'[3P-Sub/1S-inc-Obj]+'", "ᎬᎩ^"), \
            ("'[3P-Sub/1D-inc-Obj]+'", "ᎨᎩnii^"), \
            ("'[3P-Sub/1P-inc-Obj]+'", "Ꭸkii^"), \
            ("'[3P-Sub/1D-ex-Obj]+'", "ᎪᎩnii^"), \
            ("'[3P-Sub/1P-ex-Obj]+'", "Ꭺkii^"), \
            ("'[3P-Sub/2S-Obj]+'", "Ꭸja^"), \
            ("'[3P-Sub/2D-Obj]+'", "ᎨᏍtii^"), \
            ("'[3P-Sub/2P-Obj]+'", "Ꭸjii^")]

#two_local = [("'[2S-Sub/1S-Obj]+'", "ski^"), \
#            ("'[1S-Sub/2S-Obj]+'", "kvv^"), \
#            ("'[2S-Sub/1D-Obj]+'", "iiskinii^"), \
#            ("'[2D-Sub/1D-Obj]+'", "iiskinii^"), \
#            ("'[2D-Sub/1S-Obj]+'", "iiskinii^"), \
#            ("'[1S-Sub/2D-Obj]+'", "iistvv^"), \
#            ("'[1D-Sub/2D-Obj]+'", "iistvv^"), \
#            ("'[1D-Sub/2S-Obj]+'", "iistvv^"),\
#            ("'[2S-Sub/1P-Obj]+'", "iiskii^"), \
#            ("'[2D-Sub/1P-Obj]+'", "iiskii^"), \
#            ("'[2P-Sub/1P-Obj]+'", "iiskii^"), \
#            ("'[2P-Sub/1D-Obj]+'", "iiskii^"), \
#            ("'[2P-Sub/1S-Obj]+'", "iiskii^"), \
#            ("'[1S-Sub/2P-Obj]+'", "iijvv^"), \
#            ("'[1D-Sub/2P-Obj]+'", "iijvv^"), \
#            ("'[1P-Sub/2P-Obj]+'", "iijvv^"), \
#            ("'[1P-Sub/2D-Obj]+'", "iijvv^"), \
#            ("'[1P-Sub/2S-Obj]+'", "iijvv^")]

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

#object_focus = [("'[1S-inc-Obj]+'", "vvki^"), \
#            ("'[1D-inc-Obj]+'", "eekinii^"), \
#            ("'[1P-inc-Obj]+'", "eekii^"), \
#            ("'[1D-ex-Obj]+'", "ookinii^"), \
#            ("'[1P-ex-Obj]+'", "oojii^"), \
#            ("'[2S-Obj]+'", "eeja^"), \
#            ("'[2D-Obj]+'", "eestii^"), \
#            ("'[2P-Obj]+'", "eejii^"), \
#            ("'[3S-Obj]+'", "aji^"), \
#            ("'[3P-Obj]+'", "keejii^"), \
#            ("'[3P-Obj]+'", "keek^")]

    
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

Grammar = {}
Grammar["S"] = [("", "Prefix8")]

Grammar["Prefix8"] = [("", "PersonPrefixes"), \
                      (("'[NGT]+'", "kaa^"), "PersonPrefixes")]
    
Grammar["PersonPrefixes"] = fin_person

Grammar["SetA_Verbs"] = [("", "Intrans_SetA"), ("", "Trans_SetA")]
Grammar["SetB_Verbs"] = [("", "Intrans_SetB"), ("", "Trans_SetB")]
Grammar["Transitive_Verbs"] = [("", "Trans_SetA"), ("", "Trans_SetB")]

#Grammar["Intrans_SetA"] = [("wooniha", "PresCont"), \
#                           ("aaʔi", "PresCont")]

#Grammar["Intrans_SetA"] = [("ᏬᏂᎭ", "PresCont"), \
#                           ("aᎢ", "PresCont")]

Grammar["Intrans_SetA"] = [(("'ᏬᏂᎭ''+[V]''+[PresCont]'", "ᏬᏂᎭ"), "#"), \
                           (("'ᎠᎢ''+[V]''+[PresCont]'", "ᎠᎢ"), "#"), \
                           (("'ᏅᏥᏙᎭ''+[V]''+[PresCont]'", "ᏅᏥᏙᎭ"), "#")]    

#Grammar["Intrans_SetB"] = [("nvjiithl", "Comp"), \
#                           ("eeluukiisk", "Incomp")]

#Grammar["Intrans_SetB"] = [("ᏅᏥtl", "Comp"), \
#                           ("eᎷᎩᏍk", "Incomp")]

Grammar["Intrans_SetB"] = [(("'ᏅᏥᏙᎭ''+[V]''+[Completive]'", "ᏅᏥᏙl"), "Stem2and4Final"), \
                           (("'ᎡᏡᎦ''+[V]''+[PresCont]'", "ᎡᏡᎦ"), "#")]

#Grammar["Trans_SetA"] = [("steeliha", "PresCont"), \
#                         ("steeliisk", "Incomp"), \
#                         ("steela", "Immediate"), \
#                         ("ookiska", "PresCont")]

#Grammar["Trans_SetA"] = [("ᏍᏕᎵᎭ", "PresCont"), \
#                         ("ᏍᏕᎵᏍk", "Incomp"), \
#                         ("ᏍᏕᎳ", "Immediate"), \
#                         ("oᎩᏍᎦ", "PresCont")]


Grammar["Trans_SetA"] = [(("'ᏍᏕᎵᎭ''+[V]''+[PresCont]'", "ᏍᏕᎵᎭ"), "#"), \
                         (("'ᏍᏕᎵᎭ''+[V]''+[Incompletive]'", "ᏍᏕᎵᏍk"), "Habitual"), \
                         (("'ᏍᏕᎵᎭ''+[V]''+[Immediate]'", "ᏍᏕᎳ"), "#"), \
                         (("'ᎤᎢᎶᎠ''+[V]''+[PresCont]'", "ᎤᎢᎶᎠ"), "#"), \
                         (("'ᎣᎩᏍᎦ''+[V]''+[PresCont]'", "ᎣᎩᏍᎦ"), "#"), \
                         (("'ᎥᏃᏌᏍᎦ''+[V]''+[PresCont]'", "ᎥᏃᏌᏍᎦ"), "#"), \
                         (("'ᎥᏂᎭ''+[V]''+[PresCont]'", "ᎥᏂᎭ"), "#")]
    
#Grammar["Trans_SetB"] = [("steelvvh", "Comp"), \
#                         ("stehlt", "DeVerb"), \
#                         ("uuhiiloo", "Comp"), \
#                         ("vvnoosah", "Comp"), \
#                         ("vhthan", "Comp"), \
#                         ("atuuliha", "PresCont")]
    
#Grammar["Trans_SetB"] = [("ᏍᏕᎸh", "Comp"), \
#                         ("stehlt", "DeVerb"), \
#                         ("uᎯᎶʔ", "Comp"), \
#                         ("vᏃᏌh", "Comp"), \
#                         ("vᏔn", "Comp"), \
#                         ("aᏚᎵᎭ", "PresCont")]

Grammar["Trans_SetB"] = [(("'ᏍᏕᎵᎭ''+[V]''+[Completive]'", "ᏍᏕᎸh"), "Stem2and4Final"), \
                         (("'ᏍᏕᎵᎭ''+[V]''+[DeVerbalNoun]'", "stehlt"), "Stem5Final"), \
                         (("'ᎤᎢᎶᎠ''+[V]''+[Completive]'", "ᎤᎯᎶʔ"), "Stem2and4Final"), \
                         (("'ᎥᏃᏌᏍᎦ''+[V]''+[Completive]'", "ᎥᏃᏌh"), "Stem2and4Final"), \
                         (("'ᎥᏂᎭ''+[V]''+[Completive]'", "ᎥᏂl"), "Stem2and4Final"), \
                         (("'ᎠᏚᎵᎭ''+[V]''+[PresCont]'", "ᎠᏚᎵᎭ"), "#")]

#Grammar["PresCont"] = [(("'+[V]''+[PresCont]'", ""), "#")]
#Grammar["Incomp"] = [(("'+[V]''+[Incompletive]'", ""), "Habitual")]
#Grammar["Immediate"] = [(("'+[V]''+[Immediate]'", ""), "#")]
#Grammar["Comp"] = [(("'+[V]''+[Completive]'", ""), "Stem2and4Final")]
#Grammar["DeVerb"] = [(("'+[V]''+[DeVerbalNoun]'", ""), "Stem5Final")]

#Grammar["Habitual"] = [(("'+[Habitual]'", "^oʔi"), "#"), \
#                       ("", "Stem2and4Final")]

Grammar["Habitual"] = [(("'+[Habitual]'", "^ᎣᎢ"), "#"), \
                       ("", "Stem2and4Final")]

    
#Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^vvʔi"), "#"), \
#                             (("'+[NonExpPast]'", "^eʔi"), "#"), \
#                             (("'+[AbsFut]'", "^éesti"), "#")]

Grammar["Stem2and4Final"] = [(("'+[ExpPast]'", "^ᎥᎢ"), "#"), \
                             (("'+[NonExpPast]'", "^ᎡᎢ"), "#"), \
                             (("'+[AbsFut]'", "^ᎡᏍᏗ"), "#")]

#Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^i"), "#"), \
#                         (("'+[NomAbility]'", "^ííʔi"), "#")]

Grammar["Stem5Final"] = [(("'+[NomAbilityOrObligation]'", "^Ꭲ"), "#"), \
                         (("'+[NomAbility]'", "^ᎢᎢ"), "#")]

Lexicon = FST.rlg(Grammar, "S")
Lexicon = Lexicon.epsilon_remove().determinize().minimize()

fsts = {}
fsts['V'] = FST.re("[aeiouvᎠᎡᎢᎣᎤᎥ]")         # Vowels

rule1 = FST.re("$^rewrite(Ꮵ:k / _ \^ $V)", fsts)
#This stays the same
#Results in k^vowel (aeouv - verb stems don't start with /i/) needing to be rewritten

rule2 = FST.re("$^rewrite(i:y / [#|\^](Ꮵ|Ꭿ|ᎢᏍᎩ) _ \^ $V)", fsts)
#This becomes i-> in front of ji/hi and before vowel (assuming we write these endigns as (hi)i^)
#Results in y^vowel needs to be rewritten in syllabary or stray i^ that needs to be removed

rule2_1 = FST.re("$^rewrite('':y / (Ꭼ|Ꮫ|Ꮸ) _ \^ $V)", fsts)

#Write rule to remove stray [i] right here ... no this could be problematic, do it later.

rule3 = FST.re("$^rewrite(Ꭹ:(kw) / _ \^ $V)", fsts)
#change syllabary ki to transcription kw-
#results in kw^vowel needs to be rewritten

#NGT Rules
#kaa + uu = kvv^wa 
ngt1 = FST.re("$^rewrite((kaa\^Ꭴ):(Ꭼ\^wa))", fsts)

#kvv^wa^ + v = kvv^wa^
ngt2 = FST.re("$^rewrite(Ꭵ:'' / Ꭼ\^wa\^ _ )", fsts)

#Kaa + aji (ᎠᏥ^) = k^eji
ngt3 = FST.re("$^rewrite(Ꭰ:Ꭱ / kaa\^ _ (Ꮵ|k)\^ )", fsts)

#Kaa + [eiov] = kaay^ + [eiov]
ngt4 = FST.re("$^rewrite((kaa):(Ꭶy) / _ \^ [eiovᎡᎢᎣᎥ])", fsts)

#Kaa + a = kvv^
ngt5 = FST.re("$^rewrite((kaa\^(aa?|Ꭰ)):(kvv\^), longest = True, leftmost = True)", fsts)

#uu (SetB [3S-Sub/3S-inanimate-Obj])
rule4 = FST.re("$^rewrite('':w / Ꭴ _ \^ [eouᎡᎣᎤ])", fsts)
#Add roman 'w' after syllabary uu
#results in w^vowel needs to be rewritten

rule5 = FST.re("$^rewrite((Ꭴ\^Ꭵ):(ᎤᏩ\^))", fsts)
#Syllabary to syllabary

rule6 = FST.re("$^rewrite(Ꭰ:'' / Ꭴ\^ _ )", fsts)
#uu will be in syllabary, a will not

#rule7 --> Add later
cleanup1 = FST.re("$^rewrite(\^:'' / \^ _)", fsts)

rule8 = FST.re("$^rewrite((aa?|ii?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)
rule9 = FST.re("$^rewrite((vv?):'' / _ \^ $V, longest = True, leftmost = True)", fsts)
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

#Cleaned = FST.re("$^rewrite(\^:'')")

fsts['Lexicon'] = Lexicon
fsts['rule1'] = rule1
fsts['rule2'] = rule2
fsts['rule2_1'] = rule2_1
fsts['rule3'] = rule3
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
final = FST.re("$Lexicon @ $rule1 @ $rule2 @ $rule2_1 @ $rule3 @ $ngt1 @ $ngt2 @ $ngt3 @ $ngt4 @ $ngt5 @ $rule4 @ $rule5 @ $rule6 @ $cleanup1 @ $rule8 @ $rule9", fsts)


# if function == 'generate':
#     res = list(final.generate(cherokee))
# elif function == 'parse':
#     res = list(final.analyze(cherokee))
# else:
#     print("Arg1 must be either 'generate' or 'parse'")

# print(res)
# cherokee_syllabary_fin.txt
# Displaying cherokee_syllabary_fin.txt.Next 

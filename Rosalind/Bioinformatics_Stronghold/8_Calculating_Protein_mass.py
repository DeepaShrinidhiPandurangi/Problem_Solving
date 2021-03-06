#8:Calculating protein mass
# Chaining the amino acids : Calculating the weight/mass of the protein by adding the weigths of individual amino acids from the mono-isotopic mass table
protein="KIFPKEVDRMMPWLEMSEVGCGTPQHEKFYFCGNWWIKKVNSIPYWEWMLVDAEQLCKFFHKYASHQEFCTQQRWIIQEIKNHNPPGCNQHKDFCRVCGWGDGNLPTYYKIDLIKNDDQMQQESCVALNQTMYFHPMFTMLSAWNRKTQKANMDKRYLWECRAPKYFYQDQFHTAMSTTKVSQHQNEWTRMSDQNNSSQFCFWIPAMDEQTEWDCRFCNYMDCLCHRWDVRWKNTMYFVFEFYCQYFGTFVHCYKEPTILIYGMDPLPQMPDWAKVCTYFQHSWGLRPIGDTCAAMGCPFCVNPLGCYMDQGMRYATIVPKPMYISSVGFQPNPDYIGTYQGITGLNRLILMRDRLYSFYQWWRKFGCMMGRHCWDIMTTCDSQDNDGHKMCRCREKCRRTALLMNQPCAAWFAKMMEHCMSFSPCKVVPGATGSMWMFFVTNYKVAEWCWARFPTMGLEQFILAWGEMHFYQRMVTISQSEMPGVEMILRFSQEGGQQPQCLSGINVSSNQSGYLELYIRHTKFRECLPYIQEHSGEEFMAKESQFFIFWFFEPCKFWFDINLYLRRKYCHQWNAHKPIVSYFWGLVEPVYNAAMNTQFTMIYSEWTLLRMSLRHPPEQMDHMQYPMDFGNVGMCIHWGSSEHRYKHWHGQNGNAYLSEHNYGANQWIMCMTECAVTFWFQLVCWWPMKGVRPCRNMIESECESDVMKNSKYPGCFLTSMEFDNSAKMNLSGMKMCVFAYLRIEYKKQCLKDRWKERDITFPCLNLHHRMMVVFRTFDDCYKKATGSGVPMMKTFDHICCCHEMAHIDHFYNARWVVMKPCFSDWGEMCSANCCDHVTHWMLEFWYPSNGKNEPYMRNNNMEYHIHMTKYMAIKTDYHAIWVEYNSITIPEDNSRMEWEQEQFYHVEVRWAALMQMQNLAFIKCQHIMPPTNVWPWIMPFWIGSQMQCLPILWS"
mono_is_mass_table ={
"A" :71.03711,
"C" :103.00919,
"D" :115.02694,
"E" :129.04259,
"F" :147.06841,
"G" :57.02146,
"H" :137.05891,
"I" :113.08406,
"K" :128.09496,
"L" :113.08406,
"M" :131.04049,
"N" :114.04293,
"P" :97.05276,
"Q" :128.05858,
"R" :156.10111,
"S" :87.03203,
"T" :101.04768,
"V" :99.06841,
"W" :186.07931,
"Y" :163.06333 }
print(mono_is_mass_table)
protein_weight= 0
for i in protein :
  protein_weight = protein_weight + mono_is_mass_table[i]
print(round(protein_weight,3))
# PROT Translating RNA into Protein 
# RNA to amino acids (protein) codon table:
''' Table wiki link given:
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''
s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
L=[]
string = ""
codon_dict = {'UUU': "F", 'UUC': "F", 'UUA': "L", 'UUG': "L", 'UCU': "S", 'UCC': "S", 'UCA': "S", 'UCG': "S", 'UAU': "Y", 'UAC': "Y",'UAA': "Stop", 'UAG': "Stop", 'UGU': "C", 'UGC': "C", 'UGA': "Stop", 'UGG': "W",'CUU': "L", 'CUC': "L", 'CUA': "L", 'CUG': "L", 'CCU': "P", 'CCC': "P", 'CCA': "P", 'CCG': "P", 'CAU': "H", 'CAC': "H", 'CAA': "Q", 'CAG': "Q", 'CGU': "R", 'CGC': "R", 'CGA': "R",'CGG': "R", 'AUU': "I", 'AUC': "I", 'AUA': "I", 'AUG': "M", 'ACU': "T", 'ACC': "T", 'ACA': "T", 'ACG': "T", 'AAU': "N", 'AAC': "N", 'AAA': "K", 'AAG': "K", 'AGU': "S", 'AGC': "S",'AGA': "R", 'AGG': "R", 'GUU': "V", 'GUC': "V", 'GUA': "V", 'GUG': "V", 'GCU': "A", 'GCC': "A", 'GCA': "A", 'GCG': "A", 'GAU': "D", 'GAC': "D", 'GAA': "E", 'GAG': "E", 'GGU': "G",'GGC': "G", 'GGA': "G", 'GGG': "G"}
for i in range(0,len(s),3):
  code = s[i:i+3]
  #print(code)
  for key,value in codon_dict.items():
    if code == key:
      string= string+value
#print(string)
res = string.split("Stop")
print(res[0])
# output : MAMAPRTEINSTRING


# or more easy one 
s= "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
protein =""
codon_dict = {'UUU': "F", 'UUC': "F", 'UUA': "L", 'UUG': "L", 'UCU': "S", 'UCC': "S", 'UCA': "S", 'UCG': "S", 'UAU': "Y", 'UAC': "Y",'UAA': "Stop", 'UAG': "Stop", 'UGU': "C", 'UGC': "C", 'UGA': "Stop", 'UGG': "W",'CUU': "L", 'CUC': "L", 'CUA': "L", 'CUG': "L", 'CCU': "P", 'CCC': "P", 'CCA': "P", 'CCG': "P", 'CAU': "H", 'CAC': "H", 'CAA': "Q", 'CAG': "Q", 'CGU': "R", 'CGC': "R", 'CGA': "R",'CGG': "R", 'AUU': "I", 'AUC': "I", 'AUA': "I", 'AUG': "M", 'ACU': "T", 'ACC': "T", 'ACA': "T", 'ACG': "T", 'AAU': "N", 'AAC': "N", 'AAA': "K", 'AAG': "K", 'AGU': "S", 'AGC': "S",'AGA': "R", 'AGG': "R", 'GUU': "V", 'GUC': "V", 'GUA': "V", 'GUG': "V", 'GCU': "A", 'GCC': "A", 'GCA': "A", 'GCG': "A", 'GAU': "D", 'GAC': "D", 'GAA': "E", 'GAG': "E", 'GGU': "G",'GGC': "G", 'GGA': "G", 'GGG': "G"}
for i in range (0,len(s),3):
  protein = protein + codon_dict[s[i:i+3]]
protein = protein.split("Stop")
print(protein[0])
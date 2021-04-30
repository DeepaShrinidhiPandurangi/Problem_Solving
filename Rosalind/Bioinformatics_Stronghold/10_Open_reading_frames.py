#10. Open reading frames
'''http://bioweb.uwlax.edu/GenWeb/Molecular/Seq_Anal/Translation/translation.html'''
'''
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''
codon_dict = {'TTT': "F", 'TTC': "F", 'TTA': "L", 'TTG': "L", 'TCT': "S", 'TCC': "S", 'TCA': "S", 'TCG': "S", 'TAT': "Y", 'TAC': "Y",'TAA': "Stop", 'TAG': "Stop", 'TGT': "C", 'TGC': "C", 'TGA': "Stop", 'TGG': "W",'CTT': "L", 'CTC': "L", 'CTA': "L", 'CTG': "L", 'CCT': "P", 'CCC': "P", 'CCA': "P", 'CCG': "P", 'CAT': "H", 'CAC': "H", 'CAA': "Q", 'CAG': "Q", 'CGT': "R", 'CGC': "R", 'CGA': "R",'CGG': "R", 'ATT': "I", 'ATC': "I", 'ATA': "I", 'ATG': "M", 'ACT': "T", 'ACC': "T", 'ACA': "T", 'ACG': "T", 'AAT': "N", 'AAC': "N", 'AAA': "K", 'AAG': "K", 'AGT': "S", 'AGC': "S",'AGA': "R", 'AGG': "R", 'GTT': "V", 'GTC': "V", 'GTA': "V", 'GTG': "V", 'GCT': "A", 'GCC': "A", 'GCA': "A", 'GCG': "A", 'GAT': "D", 'GAC': "D", 'GAA': "E", 'GAG': "E", 'GGT': "G",'GGC': "G", 'GGA': "G", 'GGG': "G" , 'A': "",'T': "",'C': "",'G': "", 'AT': "",'AC': "",'AG': "",'TA': "",'TC': "",'TG': "",'GT': "",'GA': "",'GC': "",'CG': "",'CT': "",'CA': "",'AA': "",'TT': "",'GG': "",'CC': ""}

res_1 = res_2 = res_3 = res_4 = res_5 = res_6 = ""
string='''>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'''
import io
infile = io.StringIO(string)
for line in infile:
  line= line.strip()
  if line[0]==">":
    s= ""
  else:
    s = s+line
#print(s)

def rev_comp(s):
  s = s[::-1]
  s1 =""
  for i,j in enumerate(s):
    if j == "A":
      s1 = s1+ "T"
    elif j == "T":
      s1 = s1 + "A"
    elif j == "C":
      s1 = s1+ "G"
    elif j == "G":
      s1 = s1+ "C"
  return (s1)
r = rev_comp(s)

s_1 = s[0:len(s)]
s_2 = s[1:len(s)]
s_3 = s[2:len(s)]
r_1 = r[0:len(r)]
r_2 = r[1:len(r)]
r_3 = r[2:len(r)]
'''
print(s_1)
print(s_2)
print(s_3)
print(r_1)
print(r_2)
print(r_3)
'''

for i in range(0,len(s_1),3):
  res_1 = res_1 + codon_dict[s_1[i:i+3]]
for i in range(0,len(s_2),3):
  res_2 = res_2 + codon_dict[s_2[i:i+3]]
for i in range(0,len(s_3),3):
  res_3 = res_3 + codon_dict[s_3[i:i+3]]

for i in range(0,len(r_1),3):
  res_4 = res_4 + codon_dict[r_1[i:i+3]]
for i in range(0,len(r_2),3):
  res_5 = res_5 + codon_dict[r_2[i:i+3]]
for i in range(0,len(r_3),3):
  res_6 = res_6 + codon_dict[r_3[i:i+3]]
'''
print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)
print(res_6)
'''
x1 = res_1.split("Stop")[:-1]
x2 = res_2.split("Stop")[:-1]
x3 = res_3.split("Stop")[:-1]
x4 = res_4.split("Stop")[:-1]
x5 = res_5.split("Stop")[:-1]
x6 = res_6.split("Stop")[:-1]
'''
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
'''

L =[]# Main List

for i in x1:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
for i in x2:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
for i in x3:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
for i in x4:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
for i in x5:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
for i in x6:
  if "M" in i:
    if i[i.index("M"):] not in L:
      L.append(i[i.index("M"):])
#print(L)

L2 =[]
for i in L:
  L1 =[] # indexes of "M"
  for j in range(0,len(i)):
    if i[j]== "M":
      L1.append(j)
  #print(L1)
  for k in L1:
    L2.append(i[k:])
#print(L2)

for i in L2:
  print("*",i)
'''
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

# alternate code:
# add triple quotes before and after the string before running this code

codon_dict = {'UUU': "F", 'UUC': "F", 'UUA': "L", 'UUG': "L", 'UCU': "S", 'UCC': "S", 'UCA': "S", 'UCG': "S", 'UAU': "Y", 'UAC': "Y",'UAA': "Stop", 'UAG': "Stop", 'UGU': "C", 'UGC': "C", 'UGA': "Stop", 'UGG': "W",'CUU': "L", 'CUC': "L", 'CUA': "L", 'CUG': "L", 'CCU': "P", 'CCC': "P", 'CCA': "P", 'CCG': "P", 'CAU': "H", 'CAC': "H", 'CAA': "Q", 'CAG': "Q", 'CGU': "R", 'CGC': "R", 'CGA': "R",'CGG': "R", 'AUU': "I", 'AUC': "I", 'AUA': "I", 'AUG': "M", 'ACU': "T", 'ACC': "T", 'ACA': "T", 'ACG': "T", 'AAU': "N", 'AAC': "N", 'AAA': "K", 'AAG': "K", 'AGU': "S", 'AGC': "S",'AGA': "R", 'AGG': "R", 'GUU': "V", 'GUC': "V", 'GUA': "V", 'GUG': "V", 'GCU': "A", 'GCC': "A", 'GCA': "A", 'GCG': "A", 'GAU': "D", 'GAC': "D", 'GAA': "E", 'GAG': "E", 'GGU': "G",'GGC': "G", 'GGA': "G", 'GGG': "G","A":"","U":"","G":"","C":"","AU":"", "AC":"" ,"AG":"", "UA":"" ,"UC":"", "UG":"", "CG":"" ,"CA":"", "CU":"", "GA":"", "GU":"" ,"GC": "","GG":"","CC":"","UU":"","AA":""}
import io
s = '''>Rosalind_0284
AGGAGCTAGGCCGCGGGGCCGATATCCTCCGGTCGACTGCGTCCCCAGTTCCGCGCCCGG
CGATTGTTCCATAAATTAAATGTGTTACCCGAACCGCAAATAAGTAACCTGGTATACCGT
TAGTCAGGGCCGGGAAATCCGCAAGCCAAGCCTGCGTTGATTCGTGCTCGACCGTTCCAG
AACTCACCGAGTATCCGAGAAACCCTATGTTAACCAATAATCGCAGCTGAGCGCACTAAC
TGTTCATTACACCTAACTTGCGGCAGCATTTGCCTAGTGAGCGTCCAACGTTTATATCAC
TTCCCCCCTCTTTACAGACCGTCAACACCCCACCGGGAGGGCCATAAGCACACGCTTGTT
TTTGCAAGGTTATTACTCGCCCATGCCCGCTCGCCACACGTTGAGGTGCATATAGGCGTA
GTGACGCGGTCCATTATGAGAGCCCCAGTAGCTGGTGTTTAGCTAAACACCAGCTACTGG
GGCTCTCATCGATCAGCGTGAAGCCCCCTTACTTAGAAGAAACCCTTACCCCACCAGTAC
CCACTACGATGCGTACAAACTTGGACCTTACGAGCTTAGCGTCGATCACGAAGCTTGCTG
CCTGTGCAGTAGAGTATGCGCAATGCTATCATTCCTGCAACCTCCACAGCCCTGTAGTAG
TACTCTCCTAAAATTAAACGTCTAAACGGACGTCATCGGAGCAGCAAAGACAAATAAACG
TTTGCGCTGTGAGGGTGAGCCGCCATGGCGGTGCTCCCGACGATAGAGCTAGTCTCTGTG
CGTACTATACCTTATAAAGTCTGGTTAATTAACAGGAACACGGAGACATGCATCAAATTC
ACGCAGGTTAAAACTTGGCGCGACACTGGAAGGTGTTCTCGTTCGTTCTGCCTACTATCC
GTGCTGGGGGATATCGACCTACTC '''
s1 = io.StringIO(s)

for line in s1:
  line = line.strip()
  if line[0]== ">":
    protein =""
  else:
    protein = protein + line
#print(protein)

s2 = protein.replace("T","U")
s3 = protein[::-1]
s4= ""
for i in range(0,len(s3)):
  if s3[i] == "A":
    s4 = s4+"T"
  elif s3[i] == "T":
    s4 = s4+"A"
  elif s3[i] == "G":
    s4 = s4+"C"
  else:
    s4 = s4 +"G"
s4 = s4.replace("T","U")

pro1 = ""
for i in range(0,len(s2),3):
  pro1 = pro1 + codon_dict[s2[i:i+3]]
#print(pro1)

pro2= ""
for i in range(0,len(s2[1:]),3):
  pro2 = pro2 + codon_dict[s2[1:][i:i+3]]
#print(pro2)

pro3=""
for i in range(0,len(s2[2:]),3):
  pro3 = pro3 + codon_dict[s2[2:][i:i+3]]
#print(pro3)

pro4 = ""
for i in range(0,len(s4),3):
  pro4 = pro4 + codon_dict[s4[i:i+3]]
#print(pro4)

pro5 = ""
for i in range(0,len(s4[1:]),3):
  pro5 = pro5 + codon_dict[s4[1:][i:i+3]]
#print(pro5)

pro6 = ""
for i in range(0,len(s4[2:]),3):
  pro6 = pro6 + codon_dict[s4[2:][i:i+3]]
#print(pro6)

res =[]
pro1 = pro1.split("Stop")
pro1 = pro1[0:len(pro1)-1]
L1=[]
for i in pro1:
  if "M" in i:
    L1.append(i)
#print(L1)
pos1=[]
for i in L1:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos1.append(j)
  #print(pos1)
  for k in range(0,len(pos1)):
    res.append(i[pos1[k]:])
  pos1= []


pro2 = pro2.split("Stop")
pro2 = pro2[0:len(pro2)-1]
L2=[]
for i in pro2:
  if "M" in i:
    L2.append(i)
#print(L2)
pos2=[]
for i in L2:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos2.append(j)
  #print(pos2)
  for k in range(0,len(pos2)):
    res.append(i[pos2[k]:])
  pos2= []

pro3 = pro3.split("Stop")
pro3 = pro3[0:len(pro3)-1]
L3=[]
for i in pro3:
  if "M" in i:
    L3.append(i)
#print(L3)
pos3=[]
for i in L3:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos3.append(j)
  #print(pos3)
  for k in range(0,len(pos3)):
    res.append(i[pos3[k]:])
  pos3= []

pro4 = pro4.split("Stop")
pro4 = pro4[0:len(pro4)-1]
L4=[]
for i in pro4:
  if "M" in i:
    L4.append(i)
#print(L4)
pos4=[]
for i in L4:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos4.append(j)
  #print(pos1)
  for k in range(0,len(pos4)):
    res.append(i[pos4[k]:])
  pos4= []

pro5 = pro5.split("Stop")
pro5 = pro5[0:len(pro5)-1]
L5=[]
for i in pro5:
  if "M" in i:
    L5.append(i)
#print(L5)
pos5=[]
for i in L5:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos5.append(j)
  #print(pos5)
  for k in range(0,len(pos5)):
    res.append(i[pos5[k]:])
  pos5=[]

pro6 = pro6.split("Stop")
pro6 = pro6[0:len(pro6)-1]
L6=[]
for i in pro6:
  if "M" in i:
    L6.append(i)
#print(L6)
pos6=[]
for i in L6:
  for j in range(0,len(i)):
    if i[j]=="M":
      pos6.append(j)
  #print(pos6)
  for k in range(0,len(pos6)):
    res.append(i[pos6[k]:])
  pos6= []

res1 = []
for i in res:
  if i not in res1:
    res1.append(i)
for i in res1:
  print("&",i)


# code 3.shortest alternate
s = io.StringIO(s)
for line in s:
  line = line.strip()
  if line[0]== ">":
    s =""
  else:
    s = s + line
#print(s)
codon_dict = {'TTT': "F", 'TTC': "F", 'TTA': "L", 'TTG': "L", 'TCT': "S", 'TCC': "S", 'TCA': "S", 'TCG': "S", 'TAT': "Y", 'TAC': "Y",'TAA': "Stop", 'TAG': "Stop", 'TGT': "C", 'TGC': "C", 'TGA': "Stop", 'TGG': "W",'CTT': "L", 'CTC': "L", 'CTA': "L", 'CTG': "L", 'CCT': "P", 'CCC': "P", 'CCA': "P", 'CCG': "P", 'CAT': "H", 'CAC': "H", 'CAA': "Q", 'CAG': "Q", 'CGT': "R", 'CGC': "R", 'CGA': "R",'CGG': "R", 'ATT': "I", 'ATC': "I", 'ATA': "I", 'ATG': "M", 'ACT': "T", 'ACC': "T", 'ACA': "T", 'ACG': "T", 'AAT': "N", 'AAC': "N", 'AAA': "K", 'AAG': "K", 'AGT': "S", 'AGC': "S",'AGA': "R", 'AGG': "R", 'GTT': "V", 'GTC': "V", 'GTA': "V", 'GTG': "V", 'GCT': "A", 'GCC': "A", 'GCA': "A", 'GCG': "A", 'GAT': "D", 'GAC': "D", 'GAA': "E", 'GAG': "E", 'GGT': "G",'GGC': "G", 'GGA': "G", 'GGG': "G"}

c= s.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()[::-1]
#print(c)

s1=[]
c1=[]
for i in range(0,3):
  s1.append(s[i:len(s)])
  c1.append(c[i:len(c)])
#print(s1)
#print(c1)

L=[]
for element in s1:
  a=""
  for i in range(0,len(element),3):
    if element[i:i+3] in codon_dict:
      a=a+codon_dict[element[i:i+3]]
  #print(a)
  L.append(a)

for element in c1:
  b=""
  for i in range(0,len(element),3):
    if element[i:i+3] in codon_dict:
      b=b+codon_dict[element[i:i+3]]
  #print(b)
  L.append(b)
#print(L)

# If there is a "Stop" in the beginning/end, the list will have "" entry as the first/last element.
S=[]
res=[]
for item in L :
  for i in range(0,len(item)):
    S=item.split("Stop")
    S=S[0:-1]
  #print(S)
  for e in S:
    if "M" in e:
      res.append(e)
#print("*",res)
  
fin =[]
for i in res:
  ind = []
  for j in range(0,len(i)):
    if i[j] == "M":
      fin.append(i[j:])
#print(fin)

final=[]
for i in fin:
  if i not in final:
    final.append(i)
for j in final:
  print(j)
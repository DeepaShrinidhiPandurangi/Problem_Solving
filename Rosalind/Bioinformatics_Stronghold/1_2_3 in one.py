dna_string = input("enter the DNA:\n")
rna = dna_string.replace ('T','U',2)
print ("the transcribed RNA is:\n",rna)
A_count = dna_string.count ('A')
T_count = dna_string.count ('T')
G_count = dna_string.count ('G')
C_count = dna_string.count ('C')
print (" The number of A's are",A_count ,"\n",
       " The number of T's are",T_count ,"\n",
       " The number of G's are",G_count ,"\n",
       " The number of C's are",C_count ,"\n")
rev_string = dna_string[::-1]
print ("rev string is ",rev_string)
len_dna_string = len(rev_string)
print (len_dna_string)
index = 0
while index < len_dna_string :
    letter = rev_string[index]
    if letter == 'A':
        print('T',end='')
    elif letter == 'C':
        print('G',end='')
    elif letter == 'G':
        print('C',end='')
    elif letter == 'T':
        print('A',end='')
    index = index+1

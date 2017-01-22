file = open('rosalind_rna.txt', 'r')           #tells python to read a file
dna = file.readlines()                          #we give all of the data in the file a name so that we can work with it. remember, the data is a one item list in this case
dnastring = ''.join(dna)                        #convert list into string
rna = dnastring.replace('T','U')              #this replaces all 'T's with 'U's in the string
print (rna)

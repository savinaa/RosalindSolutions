f=open(r'C:\Users\Savina\Desktop\rosalind_dna8.txt','r')
string=f.read()
d={}
d['A']=string.count('A')
d['C']=string.count('C')
d['G']=string.count('G')
d['T']=string.count('T')
for key,value in d.items():
	print (key+' '+str(value),end=' ')

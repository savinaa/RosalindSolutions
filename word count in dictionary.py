f=open(r'C:\Users\Savina\Desktop\rosalind_ini7.txt','r')
word=f.read()
word_count=word.split()
m={}
for w in word_count:
	if w not in m:
		m[w]=0
	m[w]+=1
for key, value in m.items():
	print (key+' '+str(value))


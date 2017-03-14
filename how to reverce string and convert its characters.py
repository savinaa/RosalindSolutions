f=open(r'C:\Users\Savina\Desktop\rosalind_revc(2).txt','r')
string=f.read()
print(string)
rev=string[::-1]
print(rev)
a={'A':'t','T':'a','C':'g','G':'c'}
b={'a':'A','t':'T','c':'C','g':'G'}
for key,value in a.items():
	rev=rev.replace(key,value)
for key,value in b.items():
	rev=rev.replace(key,value)
print(rev)

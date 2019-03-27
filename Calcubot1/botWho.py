#!python
#-*-coding: utf-8-*-

dictWho={}

def nameWho(str):
	#k=''.join(open('dict.txt',encoding='utf-8'))
	#k.split('\n')
	for k in open('dict.txt',encoding='utf-8'):
		(key,value)=k.split('=',1)
		dictWho[key.strip()]=value.strip()
	return dictWho
	
	
if __name__ == '__main__':
	while True:
		print(nameWho(input()))
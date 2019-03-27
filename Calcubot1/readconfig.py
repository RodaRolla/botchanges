#!python
#-*-coding: utf-8-*-
import sqlite3
import re
configDict={}

def joj():
	print ('heh')

def readConfig(str):
	try:
		return configDict[str]
	except KeyError:
		return 'такого ключа не существует'

def openFile():
	for k in open('dict.txt',encoding='utf-8'):
		(key,value)=k.split('=',1)
		configDict[key.strip()]=value.strip()
		
	return configDict
	
if __name__ == '__main__':
	openConfig()
	#print (openConfig())
	#print (dictWho)
	print (readConfig('token'))
	readConfig('jej')


global config={}
это должно быть общим на все модули
def readConfig(fileName):
  названия переменных и фукнций должня быть понятными
  эта функция должна вернуть ЧТО?

Её вызод должен быть

config['configFile']='bot.conf'
confg=readConfig(config['configFile'])

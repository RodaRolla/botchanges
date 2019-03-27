#!python
#-*-coding: utf-8-*-
import sqlite3
import re
configfile={}
def configinfo(str):
	for k in open('configinfo.txt',encoding='utf-8'):
		(key,value)=k.split('=',1)
		configfile[key.strip()]=value.strip()
	return configfile[str]

if __name__ == '__main__':
	print(configinfo(input()))
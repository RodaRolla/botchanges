import re
def readConfigFile(configDict,configFile,excConf):
	for s in open(configFile,encoding='utf-8'):
		s=s.strip()
		print("Строка конфига '%s'" % s)
		if re.match('(\s*$)|(\s*#)',s): 
			print("комент или пустая строка '%s'" % s)
			continue
		kv=re.match('\s*(\w+)\s*=\s*([^#]*?)\s*(#.*)?$',s)
		if kv: 
			key = kv.group(1).lower()
			print('а тут ключ "%s"=>"%s" comment "%s"' % (key,kv.group(2),kv.group(3)))
			if key in conf:
				#key=re.match('([^#]*?)',kv.group(2))
				#if key != None:
				configDict[key] = kv.group(2) 
 				#else: 
				#	configDict[kv.group(1)] = conf[kv.group(1)] # если у ключа отсутсвует значение то оно берется из conf 
			##else:
				#print("Такого ключа нету в конфиг файле:",kv.group(1))  
				#excConf[kv.group(1)] = kv.group(2) # если введеен неверный ключ то выдается ошибка и ключ добавляется в excConf
				##raise Exception("Ключ отсутсвует в conf: '%s' " % key)
			#	continue
		##else:
			##raise Exception("Синтаксическая ошибка: '%s'" % s)
	return configDict,excConf
		
def showconfig(Dict):
	print(Dict)		
		
if __name__ == '__main__':
	conf={
		'token': '',
		'shorthelpfile': 'shortHelp.txt'
	}
	excConf={}
	#print (readConfigFile(conf, 'dict.txt',excConf))
	showconfig(readConfigFile(conf,'dict.txt',excConf))
#	try:
		#print(readConfigFile(conf, 'dict.txt',excConf))
#	except Exception as e:
		#print("Config error: " + str(e))
		#exit(1)
	#readConfigFile(conf, 'dict.txt',excConf)	
	#if excConf=={}:
	#	print(configDict)
	#else:
#		print (excConf)
#		print('something wrong')
from global_config import readConfigFile
import argparse
import re
def showconfig(Dict):
	print(Dict)
	




if __name__=='__main__':
	conf={
		'token': '',
		'shorthelpfile': 'shortHelp.txt',
		'help': 'longhelp'
		}
	excConf={}
	
	showconfig(readConfigFile(conf,'dict.txt',excConf))
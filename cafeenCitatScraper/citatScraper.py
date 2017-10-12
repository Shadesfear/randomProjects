#coding=utf8
import urllib.request
import subprocess
import PyPDF2
from itertools import islice
import re
import string
import time

#Initial load of webpage to see number of iterations
fp = urllib.request.urlopen("http://www.cafeen.org/")
mystr = fp.read().decode(errors = 'ignore').split('\n')


#Regular expressions to search for
r  = re.compile('<i>(.*?)</i>')
r0 = re.compile(' (.*?)\'')
r2 = re.compile('">(.*?)</td>') 

#Find the number of citats to download in the source code
for index, line in enumerate(mystr):
	if 'class="citat"' in line:
		citatNumber = str(mystr[index+2:index+3])

#Strip
#citatNumber = r0.search(citatNumber).group(1)
cIndex      = re.findall('\d+',citatNumber) 

citater     = [None]*int(cIndex[1])

#for i in range(index):
while True:


	try:
		fp = urllib.request.urlopen("http://www.cafeen.org/")
	except Exception as e:
		continue
	
	mystr = fp.read().decode(errors = 'ignore').split('\n')
	
	for index, line in enumerate(mystr):
		if 'class="citat"' in line:
			citat       = str(mystr[index+5:index+6])
			citatHvem   = str(mystr[index+9:index+10])
			citatNumber = str(mystr[index+2:index+3])


	citat       = r.search(citat).group(1)
	citatHvem   = r2.search(citatHvem).group(1)
	citatNumber = r0.search(citatNumber).group(1)
	cIndex      = re.findall('\d+',citatNumber) 


	if citater[int(cIndex[0])] == None:
		citater[int(cIndex[0])] = citatNumber + "\n" + citat + "\n" + citatHvem + "\n \n"
		print("Added citat number " + cIndex[0] + "\n number of items left " + str(citater.count(None)) + "\n")
	else:
		continue

	if None not in citater:
		break


file2 = open("CafeenCitater.txt","w")

for line in citater:
	file2.write(line)

file2.close()

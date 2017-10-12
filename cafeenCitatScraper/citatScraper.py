#coding=utf8
import urllib.request
import subprocess
import PyPDF2
from itertools import islice
import re
import string
import time
import os
import _thread
import threading

#Number of threads, can be adjustet
nthreads = 5
website = "http://www.cafeen.org/"

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      downloadCitat(citater)
      print ("Exiting " + self.name)


def connectCafeen(site):
	fp = urllib.request.urlopen(site)
	return fp


def downloadCitat(citater):

	r0 = re.compile(' (.*?)\'')
	r1  = re.compile('<i>(.*?)</i>')
	r2 = re.compile('">(.*?)</td>') 

	while None in citater:
		try:
			fp = connectCafeen(website)
		except Exception as e:
			continue
		mystr = fp.read().decode(errors = 'ignore').split('\n')
		
		for index, line in enumerate(mystr):
			if 'class="citat"' in line:
				citat       = str(mystr[index+5:index+6])
				citatHvem   = str(mystr[index+9:index+10])
				citatNumber = str(mystr[index+2:index+3])

		citat       = r1.search(citat).group(1)
		citatHvem   = r2.search(citatHvem).group(1)
		citatNumber = r0.search(citatNumber).group(1)
		cIndex      = re.findall('\d+',citatNumber) 


		if citater[int(cIndex[0])] == None:
			citater[int(cIndex[0])] = citatNumber + "\n" + citat + "\n" + citatHvem + "\n \n"
			print(str(citater.count(None)) + "\n")
		else:
			continue

	file2 = open("CafeenCitater.txt","w")
	for line in citater:
		try:
			file2.write(line)
		except Exception as e:
			pass
	file2.close()


#Initial connect to see how many files to download 
fp = connectCafeen(website)
mystr = fp.read().decode(errors = 'ignore').split('\n')
for index, line in enumerate(mystr):
	if 'class="citat"' in line:
		citatNumber = str(mystr[index+2:index+3])
cIndex      = re.findall('\d+',citatNumber) 
citater     = [None]*int(cIndex[1])




#Gemerate n number of threads.
for index, line in enumerate(range(1+nthreads)):
	thread = "thread" + str(index)
	thread = myThread(index+1,"thread"+str(index),index)
	thread.start()

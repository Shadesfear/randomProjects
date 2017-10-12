
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
print(mystr)
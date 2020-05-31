#!/usr/bin/python2
#coding: utf-8
#coded by asrock 
#git https://github.com/bitasrock

import os
import argparse
import time
from __strings__ import *

try:
	from main import *
	from __colors__ import *
except ImportError:
    print "[*] Found an error in requirements, trying to install setuptools..."
    os.system("apt-get install python-setuptools")
    print "[*] Installing requirements from: requirements.txt"
    time.sleep(2)
    os.system('pip install -r requirements.txt')

from main import *
from __colors__ import *

usage = '''
.__ .___. __..___.__..__  __ .  .   ver 0.2
[__)  |  (__ [__ [__][__)/  `|__|   
[__)  |  .__)[___|  ||  \\__.|  |    https://github.com/bitasrock/btsearch
                                
''' + '\nUsage: python btsearch.py "SEARCH"\n'

if len(sys.argv) < 2:
    exit(usage)
    if '--help' in sys.argv or '-h' in sys.argv:
        exit(usage)


parser = argparse.ArgumentParser()
parser.add_argument('"SEARCH"')
parser.add_argument('-v', '--verbose', required=False, action='store_true', default=False, help='Enable verbose')
args = parser.parse_args()
verbose = args.verbose


if verbose:
    init(verbose=True)
else:
    init()











			




			



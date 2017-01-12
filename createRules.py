import os
import sys
import subprocess

from snortOP import *

pwd = os.getcwd()
abnormalStr = sys.argv[1]
snortRule = 'alert tcp any any -> any any (content:"%s"; msg:"Match Abnormal String")' %abnormalStr

snt = snortOP(workpath = pwd)
snt.mod_local_rules(snortRule)

with open(localRulePath,'a') as fr:
	fr.write(snortRules + '\n')
restart_snort()

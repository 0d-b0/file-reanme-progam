#!/usr/bin/env python2
#
#   Dimitri Bourilkov  07-Feb-2016
#   Denis Burilkov     07-Feb-2016
#
# read the src file argv[1]
# from tree argv[2] to tree argv[3]
#
import os, sys, string
fname = sys.argv[1]
treein = sys.argv[2]
treeout = sys.argv[3]
fnamein = treein + "/" + fname
fnameout = treeout + "/" + fname
print()
print('>> Input  file ',fnamein)
print('>> Output file ',fnameout)
print()
fobj = open(fnamein,'r')
fobjout = open(fnameout,'w')

strin = 'semi'
strout = 'minibus_paz'

i=0
ichanged=0
debug=1

# read line by line
while 1:
    line = fobj.readline()  # read a one-line string
    if not line:            # or an empty string at EOF
        break

    i = i + 1

    # find strings
    if line.find(strin) != -1:
        ichanged=ichanged+1

    # replace strings
    lineout = line.replace(strin,strout)
    fobjout.write(lineout)


print('>> Lines processed ',i,'  lines changed ',ichanged)

# cmdline = "mv " + fnamein +  " "  + fnamein + ".orig"
# if debug == 1: print cmdline
# os.system(cmdline)
# cmdline = "mv " + fnameout +  " "  + fnamein
# if debug == 1: print cmdline
# os.system(cmdline)


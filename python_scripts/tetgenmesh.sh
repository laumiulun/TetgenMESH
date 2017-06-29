#!/usr/bin/env python3
import sys, os 


x=os.getcwd()
y=os.path.join(x,'python_scripts')

sys.path.append(y)
import runtest

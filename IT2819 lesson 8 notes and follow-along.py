# lesson 8 follow-along
# built-in functions: stuff like print(), input(), len()
# standard library: modules/groups of related functions
# must be imported before use

import random
print(random.randint(1,10))

# gotta type module name before function (unless it's a built-in)
# you can do multiple imports on one line:
import sys, os, math

#with the *, you don't have to write out the library/module first

from random import *
print(randint(1,10))

#but using the library name makes code more readable.

#to stop a program:
#sys.exit()
print('Gooddbye')
#that last line won't print
#(hmm, plain old exit() will also give an alert saying the program is ended.

#there are third-party modules too. install using "pip" program, from command line.
#check appendix A for instructions. pip itself is already installed on windows.
#to install a module: pip install <name of module> 

import pyperclip
#hmm... error message. my research and attempts to fix aren't working.
#check again when fresh

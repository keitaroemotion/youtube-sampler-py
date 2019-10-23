#!/usr/bin/env python

import sys
import subprocess


options = [x for x in sys.argv if x.startswith("-")]

def syscall(cmds, error_message=''):
    try:
        output = subprocess.check_output(cmds.split(' '))
    except:
        print("\n%s\n" % error_message)
        sys.exit()

syscall("which youtube-dl", "Command does not exist. You need to install youtube-dl")



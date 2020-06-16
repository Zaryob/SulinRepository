#!/usr/bin/env python3

import os
import os.path

def postInstall():
    os.system("""
    for i in $(busybox --list)
    do
	if which $i &>/dev/null ; then
		true
	else
		ln -s $(which busybox) /usr/bin/$i
	fi
    done
    """)
   
def postRemove():
    pass
    
def preRemove():
    pass

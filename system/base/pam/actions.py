#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
import os

def resetenv():
    os.environ.clear()
    os.environ["PATH"]="/bin:/usr/bin:/usr/sbin:/sbin"
    
def run(cmd):
    print(cmd)
    i=os.system(cmd)
    if i!=0:
        exit(i)
def setup():
    lib=("32" if get.buildTYPE()=="emul32" else "")
    resetenv()
    if lib =="32":
        os.environ["CFLAGS"]="-m32"
        os.environ["CXXFLAGS"]="-m32"
        os.environ["LDFLAGS"]="-m32"
    run("sed -e 's/pam_rhosts//g' -i modules/Makefile.am")
    run(" autoreconf -fvi")
    run("./configure --libdir=/usr/lib{0} \
                         --disable-nls \
                         --disable-db \
                         --disable-selinux \
                         --enable-securedir=/lib{0}/security \
                         --enable-isadir='.'".format(lib))

def build():
    resetenv()

    os.system("make")

def check():
    resetenv()
    run("make check")

    # dlopen check
    run("./dlopen-test.sh")

def install():
    pkgdir=get.installDIR()
    resetenv()
    run("make install DESTDIR=%s" % pkgdir)

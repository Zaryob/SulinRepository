#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

libversion = get.srcVERSION()

def build():
    autotools.make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC"' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    autotools.make('CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" -f Makefile-libbz2_so' % get.CFLAGS())

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    # No static libs
    inarytools.removeDir("/usr/lib")
    inarytools.domove("/usr/bin/", "/")
    inarytools.domove("/usr/man", "/usr/share")

    for link in ("/bin/bunzip2", "/bin/bzcat"):
        inarytools.remove(link)
        inarytools.dosym("bzip2", link)

    for wrong_link in ("/bin/bzcmp", "/bin/bzegrep", "/bin/bzfgrep", "/bin/bzless"):
        inarytools.remove(wrong_link)

    inarytools.dosym("bzgrep", "/bin/bzegrep")
    inarytools.dosym("bzgrep", "/bin/bzfgrep")
    inarytools.dosym("bzdiff", "/bin/bzcmp")
    inarytools.dosym("bzmore", "/bin/bzless")

    inarytools.dolib("libbz2.so.%s" % libversion, "/lib")

    inarytools.dosym("libbz2.so.1", "/lib/libbz2.so")
    inarytools.dosym("libbz2.so.%s" % libversion, "/lib/libbz2.so.1")

    inarytools.dohtml("manual.html")
    inarytools.dodoc("README", "CHANGES", "bzip2.txt")

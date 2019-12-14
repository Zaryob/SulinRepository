#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

exampledir = "/%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.doman("doc/man/man3/*.3")
#    inarytools.dohtml("doc/html/*")
    inarytools.dodoc("README.md")

    for i in shelltools.ls("doc/*"):
        if shelltools.isFile(i):
            inarytools.dodoc(i)

    inarytools.dodir(exampledir)
    for i in shelltools.ls("sample/*"):
        if i.endswith(".h") or i.endswith(".c"):
            inarytools.insinto(exampledir, i)

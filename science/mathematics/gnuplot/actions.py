#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gihdir=/usr/share/gnuplot \
                         --with-readline=gnu \
                         --with-X11 \
                         --with-qt=5 \
                         --with-gtk=3 \
                         --with-wx-single-threaded ")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    # Docs, Demo, Manual and Tutorial files
    inarytools.insinto("/usr/share/doc/%s/demo" % get.srcNAME(), "demo/*")
    inarytools.remove("/usr/share/doc/%s/demo/Makefile*" % get.srcNAME())
    #inarytools.insinto("/usr/share/doc/%s/manual" % get.srcNAME(), "docs/gnuplot.pdf")
    #inarytools.insinto("/usr/share/doc/%s/tutorial" % get.srcNAME(), "tutorial/*.pdf")

    inarytools.dodoc("BUGS", "ChangeLog", "FAQ.pdf", "NEWS", "README*")

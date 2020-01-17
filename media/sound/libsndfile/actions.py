#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    options = "--disable-static \
               --enable-flac \
               --enable-alsa \
               --enable-largefile \
              "

    inarytools.dosed("examples/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")
    inarytools.dosed("tests/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    shelltools.unlink("M4/libtool.m4")

    for i in shelltools.ls("M4/lt*.m4"):
        shelltools.unlink(i)

    autotools.autoreconf("-fi -I M4")
    autotools.configure(options)

    inarytools.dosed("doc/Makefile", "^htmldocdir.*", "htmldocdir = /usr/share/doc/%s/html" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

#!/usr/bin/python
# -*- coding: utf-8 -*-

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
#    autotools.autoreconf("-fvi")
    autotools.configure("--enable-utf8 \
                         --enable-color \
                         --with-slang\
                         --enable-nanorc \
                         --enable-multibuffer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.insinto("/etc/", "doc/sample.nanorc", "nanorc")
    inarytools.dosym("/usr/bin/nano", "/bin/nano")

    inarytools.dohtml("doc/*.html")
    inarytools.dodoc("ChangeLog*", "README", "doc/sample.nanorc", "AUTHORS", "NEWS", "TODO", "COPYING*", "THANKS")

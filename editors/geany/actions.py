#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
        inarytools.dosed("scripts/gen-api-gtkdoc.py", "python", "python3")
        autotools.configure("PYTHON=python3 \
                            --prefix=/usr \
                            --enable-gtk3 \
                            --enable-gtkdoc-header")
        inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
        autotools.make()

def install():
        inarytools.dodoc('AUTHORS', 'ChangeLog',
                        'COPYING', 'HACKING', 'INSTALL', 'NEWS', 'README',
                        'README.I18N', 'README.Packagers', 'THANKS', 'TODO')
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())

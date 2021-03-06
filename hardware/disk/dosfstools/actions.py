#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools


def setup():
    autotools.configure("--prefix=/usr \
                        --libexecdir=/usr/lib \
                        --sbindir=/usr/bin \
                        --mandir=/usr/share/man \
                        --docdir=/usr/share/doc/dosfstools \
                        --enable-compat-symlinks")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-3.0.txt


from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "ladspa_sdk_1.15/src"

def setup():
    inarytools.dosed("Makefile", "-Werror", get.CFLAGS())

def build():
    autotools.make('CC="%s" \
                    CXX="%s" \
                    LD="%s" \
                    targets' % (get.CC(), get.CXX(), get.LD()))

def install():
    autotools.install('INSTALL_PLUGINS_DIR="/usr/lib/ladspa" \
                       MKDIR_P="mkdir -p" \
                       DESTDIR="%s"' % get.installDIR())

    shelltools.cd("..")
    inarytools.dohtml("doc/*.html")
    inarytools.dodoc("doc/COPYING","doc/ladspa.h.txt")

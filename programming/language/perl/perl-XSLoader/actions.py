#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure("PERL_USE_UNSAFE_INC=1 \
                           PERL_MM_USE_DEFAULT=1")

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    inarytools.dodoc("MANIFEST", "Changes")
    inarytools.removeDir("/usr/share/man/*")

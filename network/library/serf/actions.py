#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import scons

def build():
    scons.make("PREFIX=/usr/ LIBDIR=/usr/lib GSSAPI=/usr/bin/krb5-config")

def install():
    inarytools.insinto("/usr/include/serf-1/", "serf*.h")
    inarytools.insinto("/usr/lib/", "libserf-1*")
    inarytools.insinto("/usr/lib/pkgconfig/", "serf-1.pc")
    
    inarytools.dodoc("CHANGES", "LICENSE", "NOTICE", "README")

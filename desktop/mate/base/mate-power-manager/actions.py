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
    #autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
			 --enable-applets \
                         --with-gtk3 \
		       	--enable-applets \
	        	--disable-strict \
	        	--without-keyring")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    inarytools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")

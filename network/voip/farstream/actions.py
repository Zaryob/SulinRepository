#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --prefix=/usr \
                         --with-html-dir=/%s/%s/html \
                         --with-package-name='Sulin farstream package' \
                         --with-package-origin='http://www.inarylinux.org'"
                         % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "INSTALL", "COPYING", "NEWS", "README")

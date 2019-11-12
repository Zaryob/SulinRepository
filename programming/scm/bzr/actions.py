#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import pythonmodules

def build():
    pythonmodules.compile()
    autotools.make("docs")

def install():
    pythonmodules.install()

    inarytools.insinto("/etc/bash_completion.d/", "contrib/bash/bzr")
    inarytools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "doc/*")

    inarytools.dodoc("COPYING.txt", "README", "NEWS", "TODO")
    shelltools.unlinkDir("{}/usr/man/".format(get.installDIR()))

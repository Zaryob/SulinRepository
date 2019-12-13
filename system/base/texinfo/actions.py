#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

TEX="/usr/share/texmf"

def setup():
    autotools.configure()

def build():
    autotools.make("TEXMF=TEX install-tex")

def install():
    inarytools.insinto("/usr/share/texmf", "%s/%s-%s/doc/TEX/tex" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    
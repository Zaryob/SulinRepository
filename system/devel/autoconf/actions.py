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
    # Fixup version
    shelltools.echo(".version", get.srcVERSION().split("_")[0])

    # Disable emacs scripts
    shelltools.export("EMACS", "no")

    autotools.configure()

def build():
    autotools.make()

# takes too long, do it by hand
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # binutils installs this infopage
    inarytools.remove("/usr/share/info/standards.info")

    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog*", "NEWS", "README")

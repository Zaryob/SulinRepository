#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import get

def setup():
    inarytools.dosed("fslint-gui","liblocation=os.path.*","liblocation = \'/usr/share/%s\'" % get.srcNAME())
    inarytools.dosed("fslint-gui","locale_base=.*","locale_base = None")

def install():
    # GUI executable
    inarytools.dobin("fslint-gui")

    insinto_dict = {# GUI file
            "/usr/share/fslint" : "fslint.glade",
            # icon
            "/usr/share/pixmaps" : "fslint_icon.png",
            # shortcut
            "/usr/share/applications" : "fslint.desktop"
            }

    for i in insinto_dict:
        inarytools.insinto(i, insinto_dict[i])

    dobin_dict= { # other executables
            "/usr/share/fslint/fslint" : ["fslint/find*", "fslint/zipdir", "fslint/fslint"] ,
            "/usr/share/fslint/fslint/fstool" : ["fslint/fstool/*"] ,
            "/usr/share/fslint/fslint/supprt" : ["fslint/supprt/get*", "fslint/supprt/fslver", "fslint/supprt/md5sum_approx"] ,
            "/usr/share/fslint/fslint/supprt/rmlint" : ["fslint/supprt/rmlint/*"] ,
            }

    for i in dobin_dict:
        inarytools.dodir(i)
        for j in dobin_dict[i]:
            inarytools.dobin(j, i)

    # locales
    shelltools.touch("Makefile")
    autotools.rawInstall("DESTDIR=%s -C po" % get.installDIR())

    # docs
    inarytools.dodoc("doc/*")

    # man files
    for i in ["man/fslint-gui.1", "man/fslint.1"]:
        inarytools.doman(i)

    # link to icon in main fslint dir
    inarytools.dosym("/usr/share/pixmaps/fslint_icon.png", "/usr/share/fslint/fslint_icon.png")


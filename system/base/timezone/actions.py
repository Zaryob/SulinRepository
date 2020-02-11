#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "."

ZoneDir = "/usr/share/zoneinfo"
TargetDir = "%s%s" % (get.installDIR(), ZoneDir)

RightDir = "%s/right" % TargetDir
PosixDir = "%s/posix" % TargetDir


timezones = ["etcetera", "southamerica", "northamerica", "europe", "africa", "antarctica", \
             "asia", "australasia", "factory", "backward", "pacificnew", \
             "systemv" ]

def setup():
    inarytools.dodir (ZoneDir)
    inarytools.dodir (RightDir)
    inarytools.dodir (PosixDir)


def install():
    inarytools.insinto ("/usr/share/zoneinfo", "iso3166.tab")
    inarytools.insinto ("/usr/share/zoneinfo", "zone.tab")
    inarytools.insinto ("/usr/share/zoneinfo", "zone1970.tab")
   
    for tzdata in timezones:
        cmd = "zic -L /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (TargetDir, get.workDIR(), tzdata)
        shelltools.system (cmd)
        part2 = "zic -L /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (PosixDir, get.workDIR(), tzdata)
        shelltools.system (part2)
        part3 = "zic -L leapseconds -d %s -y \"%s/yearistype.sh\" %s" % (RightDir, get.workDIR(), tzdata)
        shelltools.system (part3)
        #shelltools.system ("zic -d %s -y \"%s/yearistype.sh\" %s -p Europe/Istanbul" % (TargetDir, get.workDIR(), tzdata))

    shelltools.system ("zic -d %s -p Europe/Istanbul" % TargetDir)
    shelltools.system ("rm -rf {}/var/".format(get.installDIR()))
    



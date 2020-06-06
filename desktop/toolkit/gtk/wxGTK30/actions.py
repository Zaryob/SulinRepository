# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-fno-strict-aliasing")

    autotools.configure()

def build():
    autotools.make()
    autotools.make("-C locale allmo")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/usr/share/locale")
    for i in ["/usr/bin/wx-config","/usr/bin/wxrc","/usr/share/aclocal/wxwin.m4","/usr/share/bakefile/presets/wx_unix.bkl","/usr/share/bakefile/presets/wx.bkl","/usr/share/bakefile/presets/wx_presets.py","/usr/share/bakefile/presets/wx_xrc.bkl","/usr/share/bakefile/presets/wx_win32.bkl"]:
        inarytools.remove(i)

    inarytools.dodoc("docs/*.txt", "docs/*.htm")

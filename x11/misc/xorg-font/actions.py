# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "."
NoStrip = ["/"]

def setup():
    for package in shelltools.ls("*-*"):
        shelltools.cd(package)
        option = "--with-fontrootdir=/usr/share/fonts"
        autotools.configure(option)
        shelltools.cd("../")

def build():
    for package in shelltools.ls("*-*"):
        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("*-*"):
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")

    fontpaths = {
        "misc"      : "misc:unscaled:pri=10",
        "75dpi"     : "75dpi:unscaled",
        "100dpi"    : "100dpi:unscaled",
        "cyrillic"  : "cyrillic",
    }

    for fontdir, sym in fontpaths.items():
        fontpath = "/usr/share/fonts/%s" % fontdir
        inarytools.dosym(fontpath, "/etc/X11/fontpath.d/%s" % sym)

    inarytools.remove("/usr/share/fonts/*/fonts.dir")

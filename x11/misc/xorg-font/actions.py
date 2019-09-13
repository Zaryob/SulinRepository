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
        autotools.configure("--with-fontrootdir=/usr/share/fonts")
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

    # Trailing slash is important since it is used with dosed.
    encodingsDir = "/usr/share/fonts/encodings/"

    # Create encodings.dir scanning installed files only
    encdir = get.installDIR() + encodingsDir
    shelltools.system("/usr/bin/mkfontdir -n -e %s -e %slarge ." % (encdir, encdir))
    inarytools.dosed("encodings.dir", encdir, "")
    inarytools.insinto(encodingsDir, "encodings.dir")

    fontpaths = {
        "misc"      : "misc:unscaled:pri=10",
        "75dpi"     : "75dpi:unscaled",
        "100dpi"    : "100dpi:unscaled",
        "cyrillic"  : "cyrillic",
    }

    for fontdir, sym in fontpaths.items():
        fontpath = "/usr/share/fonts/%s" % fontdir
        inarytools.dosym(fontpath, "/etc/X11/fontpath.d/%s" % sym)

    # These will be generated by the package handler in xorg-app package
    inarytools.remove("/usr/share/fonts/*/fonts.dir")

# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

#WorkDir = "mozjs%s/js/src" % get.srcVERSION()

def setup():
   shelltools.cd("js/src")

   autotools.rawConfigure()

def build():
    shelltools.cd("js/src")
    autotools.make()

def install():
    shelltools.cd("js/src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #for polkit
    inarytools.domove("/usr/local/*", "/usr")
    inarytools.rename("/usr/lib/pkgconfig/mozjs-52.pc", "mozjs-17.0.pc")
    inarytools.removeDir("/usr/local")

    inarytools.dodoc("README*")

    # add link for polkit
    inarytools.dosym("libmozjs-52.so", "/usr/lib/libmozjs-17.0.so")

# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "xf86-video-sis-%s" % get.srcVERSION()

def setup():
    inarytools.dosed("src/Makefile.am", "sis_drv", "sisimedia_drv")
    inarytools.dosed("src/sis.h", '"sis"', '"sisimedia"')
    inarytools.dosed("src/sis_driver.c", "sisModuleData", "sisimediaModuleData")

    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # Same as sis man page
    inarytools.removeDir("/usr/share/man")

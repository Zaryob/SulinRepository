#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

cpupower_arch = get.ARCH().replace("i686", "i386")

def build():
    # Build cpupowertools
    shelltools.cd("tools/power/cpupower")
    autotools.make("CPUFREQ_BENCH=false")
    autotools.make("-C debug/%s centrino-decode powernow-k8-decode" % cpupower_arch)

def install():
    # Install cpupowertools stuff
    shelltools.cd("tools/power/cpupower")
    autotools.install("DESTDIR=%s libdir=/usr/lib mandir=/%s CPUFREQ_BENCH=false" % (get.installDIR(), get.manDIR()))

    inarytools.dobin("debug/%s/centrino-decode" % cpupower_arch)
    inarytools.dobin("debug/%s/powernow-k8-decode" % cpupower_arch)
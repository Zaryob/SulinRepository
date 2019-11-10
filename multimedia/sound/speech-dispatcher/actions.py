#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's/cicero //g' configure.ac")
    shelltools.system("sed -i 's/sd_cicero//g' src/modules/Makefile.am")
    
    autotools.autoreconf("-i")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --without-flite \
                         --with-alsa \
                         --with-espeak \
                         --with-libao \
                         --with-pulse \
                         --with-default-audio-method=alsa")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    # Conflicts with openTTS
    inarytools.remove("/usr/share/info/ssip.info")

    # Set executable bit
    #shelltools.chmod("%s/usr/lib/python3.6/site-packages/speechd/_test.py" % get.installDIR(), 0o755)

    # Create log directory, it should be world unreadable
    inarytools.dodir("/var/log/speech-dispatcher")
    shelltools.chmod("%s/var/log/speech-dispatcher" % get.installDIR(), 0o700)

    inarytools.dodoc("AUTHORS", "COPYING", "README")

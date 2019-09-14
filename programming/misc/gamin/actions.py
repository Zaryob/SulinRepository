#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

import os

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-inotify")

    for root, dirs, files in os.walk(get.workDIR()):
        for name in files:
            if name.endswith(".py"):
                inarytools.dosed("%s/%s" % (root, name), "#!/usr/bin/env python", "#!/usr/bin/env python3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove static lib.
    inarytools.remove("/usr/lib/libgamin_shared.a")

    inarytools.dodoc("AUTHORS", "README", "COPYING", "NEWS", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

import os

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --with-rpmbuild=/bin/false \
                         --with-drivers=all \
                         --enable-nls \
                         --without-aalib \
                         --disable-rpath \
                         --disable-lockdev \
                         --disable-resmgr \
                         --disable-ttylock \
                         --disable-baudboy \
                         --disable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          udevscriptdir=/lib/udev" % get.installDIR())

    HAL_FDI="usr/share/hal/fdi/information/20thirdparty/10-camera-libgphoto2.fdi"
    UDEV_RULES="lib/udev/rules.d/40-libgphoto2.rules"
    CAM_LIST="usr/lib/libgphoto2/print-camera-list"
    CAM_LIBS="usr/lib/libgphoto2/%s" % get.srcVERSION()

    # Create hal directory
    inarytools.dodir(shelltools.dirName(HAL_FDI))

    # Export the necessary env variables
    shelltools.export("CAMLIBS", "%s/%s" % (get.installDIR(), CAM_LIBS))
    shelltools.export("LIBDIR", "%s/usr/lib/" % get.installDIR())
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/lib/" % get.installDIR())

    # Generate HAL FDI file
    f = open(os.path.join(get.installDIR(), HAL_FDI), "w")
    f.write(os.popen("%s/%s hal-fdi" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    # Generate UDEV rule which will replace the HAL FDI when HAL is deprecated
    inarytools.dodir("/lib/udev/rules.d")
    f = open(os.path.join(get.installDIR(), UDEV_RULES), "w")
    f.write(os.popen("%s/%s udev-rules version 136" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    inarytools.removeDir("/usr/share/doc/libgphoto2_port")
    inarytools.removeDir("/usr/share/libgphoto2_port")

    # Remove circular symlink
    inarytools.remove("/usr/include/gphoto2/gphoto2")

    inarytools.dodoc("ChangeLog", "NEWS*", "README", "AUTHORS", "TESTERS", "MAINTAINERS", "HACKING")

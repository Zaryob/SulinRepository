# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ChangeLog", "COPYING", "README")
    #fix conflict with 
    for i in ["libXtst.so.6","libXtst.so.6.1.0","libXtst.so"]:
        inarytools.remove("/usr/lib/"+i)
    for i in ["/usr/include/X11/extensions/XTest.h","/usr/include/X11/extensions/record.h","/usr/lib/pkgconfig/xtst.pc","/usr/lib32/pkgconfig/xtst.pc","/usr/share/doc/libXtst/xtestlib.xml","/usr/share/doc/libXtst/recordlib.xml","/usr/share/man/man3/XTestSetVisualIDOfVisual.3","/usr/share/man/man3/XTestCompareCurrentCursorWithWindow.3","/usr/share/man/man3/XTestGrabControl.3","/usr/share/man/man3/XTestSetGContextOfGC.3","/usr/share/man/man3/XTestFakeMotionEvent.3","/usr/share/man/man3/XTestDiscard.3","/usr/share/man/man3/XTestQueryExtension.3","/usr/share/man/man3/XTestFakeKeyEvent.3","/usr/share/man/man3/XTestCompareCursorWithWindow.3","/usr/share/man/man3/XTestFakeButtonEvent.3","/usr/share/man/man3/XTestFakeRelativeMotionEvent.3"]:
        inarytools.remove(i)

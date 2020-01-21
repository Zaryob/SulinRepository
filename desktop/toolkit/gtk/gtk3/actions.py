#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import get
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools


shelltools.export("CFLAGS","")
shelltools.export("CXXFLAGS","")
shelltools.export("LDFLAGS","")

if get.buildTYPE()=="emul32":
    shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")


def setup():
    mesontools.meson_configure("-Dbroadway_backend=true -Dx11_backend=true -Dcolord=yes -Dgtk_doc=false -Dman=true")

def build():
    mesontools.ninja_build()


def install():
    mesontools.ninja_install()
    if get.buildTYPE() != "emul32":
        inarytools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")

        for binaries in ["gtk-query-immodules-3.0", "gtk-builder-tool",
                         "gtk-encode-symbolic-svg",
                         "gtk-launch", "gtk-query-settings"]:
            inarytools.dobin("inaryPackageBuild/gtk/%s" % binaries)

        inarytools.dobin("inaryPackageBuild/gtk/gtk-update-icon-cache", "/usr/bin/gtk3-update-icon-cache")

        inarytools.dobin("inaryPackageBuild/gdk/broadway/broadwayd")
        inarytools.dobin("inaryPackageBuild/demos/icon-browser/gtk3-icon-browser")
        inarytools.dobin("inaryPackageBuild/demos/gtk-demo/gtk3-demo-application")
        inarytools.dobin("inaryPackageBuild/demos/widget-factory/gtk3-widget-factory")
    else:
        inarytools.dobin("inaryPackageBuild/gtk/gtk-query-immodules-3.0", "/usr/bin/gtk-query-immodules-3.0-32bit")

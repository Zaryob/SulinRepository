# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    # Do not rebuild docs
    shelltools.export("HASDOCBOOK", "no")
    
    libtools.libtoolize("-f")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-docs \
                         --with-cache-dir=/var/cache/fontconfig \
                         --with-default-fonts=/usr/share/fonts \
                         --with-add-fonts=/usr/local/share/fonts")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.insinto("/etc/fonts", "fonts.conf", "fonts.conf.new")

    enabled_configs = ("10-sub-pixel-rgb.conf", "70-yes-bitmaps.conf")
    disabled_configs = ("10-no-sub-pixel.conf",)

    for cfg in enabled_configs:
        inarytools.dosym("../conf.avail/%s" % cfg, "/etc/fonts/conf.d/%s" % cfg)

    for cfg in disabled_configs:
        inarytools.remove("/usr/share/fontconfig/conf.avail/%s" % cfg)

    for i in ["fc-cat", "fc-list", "fc-match", "fc-cache"]:
        inarytools.doman("%s/*.1" % i)

    inarytools.doman("doc/*.3")

    inarytools.dodoc("AUTHORS", "COPYING", "README", "doc/*.txt")

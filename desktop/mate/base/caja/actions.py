#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools
def setup():
    autotools.configure("--disable-static \
                         --enable-unique \
                         --with-gnu-ld \
                         --with-gtk=3.0")   

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # fix file conflict with shared-mime-info
    for file in [ "subclasses", "XMLnamespaces", "version", "treemagic", "magic" , "aliases", "types", "globs", "globs2", "generic-icons", "mime.cache", "icons"]:
        shelltools.system("rm -f {}/usr/share/mime/{}".format(get.installDIR(),file))

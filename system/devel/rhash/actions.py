# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system("./configure --prefix=/usr \
                                   --sysconfdir=/etc \
                                   --enable-lib-shared \
                                   --enable-gettext ")
    
def install():
    autotools.make("PREFIX=/usr DESTDIR=%s build-shared install-gmo install-lib-shared" % get.installDIR())
    autotools.make("PREFIX=/usr DESTDIR=%s -C librhash install-lib-headers install-so-link" % get.installDIR())
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    
    inarytools.dodoc("ChangeLog", "INSTALL*", "README*", "COPYING*")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import cmaketools

WorkDir= "mariadb-10.4.8-linux-glibc_214-x86_64"

def install():
    inarytools.insinto("/usr/include" , "include/*")
    inarytools.insinto("/usr/lib" , "lib/*")
    inarytools.insinto("/usr/bin", "bin/*")
    inarytools.insinto("/usr/scripts", "scripts/*")
    inarytools.insinto("/usr/bin", "support-files/mysql.server")
    inarytools.insinto("/usr/bin", "support-files/wsrep_notify")
    inarytools.insinto("/etc/mysql/", "support-files/wsrep.cnf")
    inarytools.insinto("/usr/share/mysql", "share/*")
    inarytools.insinto("/usr/share/aclocal", "share/aclocal/*")
    inarytools.dosed("share/pkgconfig/mariadb.pc", "usr/local/mysql","usr")
    inarytools.dosed("share/pkgconfig/mariadb.pc", "/share","/share/mysql")
    inarytools.insinto("/usr/lib/pkgconfig", "share/pkgconfig/mariadb.pc")
    inarytools.insinto("/usr/mysql-test", "mysql-test/*")

    inarytools.doman("man/man1/*", pageDirectory="1")
    inarytools.doman("man/man8/*", pageDirectory="8")
    inarytools.dodoc("docs/*")

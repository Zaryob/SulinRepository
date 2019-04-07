# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --prefix=/usr \
                         --datadir=/usr/share/kbd \
                         --mandir=/usr/share/man")

def build():
    autotools.make("KEYCODES_PROGS=yes RESIZECONS_PROGS=yes")

def install():
    autotools.rawInstall("KEYCODES_PROGS=yes RESIZECONS_PROGS=yes DESTDIR=%s" % get.installDIR())

    for exe in ("loadkeys", "setfont", "unicode_start", "unicode_stop"):
        inarytools.domove("/usr/bin/%s" % exe, "/bin")
        inarytools.dosym("/bin/%s" % exe, "/usr/bin/%s" % exe)

    inarytools.remove("/usr/share/kbd/keymaps/i386/qwerty/trf.map.gz")

    inarytools.dohtml("docs/doc/*.html")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

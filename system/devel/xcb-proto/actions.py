# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    args='../configure \
            --prefix=/{0} \
            --build={1} \
            --mandir=/{2} \
            --infodir=/{3} \
            --datadir=/{4} \
            --sysconfdir=/{5} \
            --localstatedir=/{6} \
            --libexecdir=/{7} \
            --libdir=/usr/lib '.format(get.defaultprefixDIR(), get.HOST(), get.manDIR(),
                                        get.infoDIR(), get.dataDIR(), get.confDIR(),
                                        get.localstateDIR(), get.libexecDIR())
    shelltools.makedirs("build-python3")
    shelltools.cd("build-python3")
    shelltools.system(args + "PYTHON=/usr/bin/python3 --with-python")
    shelltools.cd("..")
    shelltools.makedirs("build-python2")
    shelltools.cd("build-python2")
    shelltools.system(args + "PYTHON=/usr/bin/python2 --with-python")

def build():
    shelltools.cd("build-python3")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("build-python2")
    autotools.make()

def check():
    shelltools.cd("build-python3")
    autotools.make("check")
    shelltools.cd("..")
    shelltools.cd("build-python2")
    autotools.make("check")

def install():
    shelltools.cd("build-python3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    shelltools.cd("build-python2")
    autotools.rawInstall("DESTDIR=%s/python2" % get.installDIR())
    shelltools.move("%s/python2/usr/lib/python2.7" % get.installDIR(),
                    "%s/usr/lib/" % get.installDIR())
    shelltools.unlinkDir("%s/python2" % get.installDIR())
    shelltools.cd("..")
    inarytools.dodoc("doc/*.txt", "COPYING", "NEWS", "README.md", "TODO")

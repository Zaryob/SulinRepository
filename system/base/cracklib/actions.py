#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("sed -i '/skipping/d' util/packer.c")
    autotools.autoreconf("-vfi")
    autotools.configure("--with-default-dict=/usr/share/cracklib/pw_dict \
                         --prefix=/usr    \
                         PYTHON={} \
                         --with-python \
                         --disable-static".format(
                         "python2" if get.buildTYPE()=="rebuild_python" else "python3.7"))

    # for unused
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("all")

def install():
    if get.buildTYPE()=="rebuild_python":
        autotools.rawInstall("DESTDIR={}/python2".format(get.installDIR()))
        shelltools.move("{}/python2/usr/lib/python2.7".format(get.installDIR()),
         "{}/usr/lib/python2.7".format(get.installDIR()))
        shelltools.unlinkDir("{}/python2/".format(get.installDIR()))
        return

    autotools.install()

    shelltools.system("install -v -m644 -D ../cracklib-words-2.9.7.gz \
                         {}/usr/share/dict/cracklib-words.gz".format(get.installDIR()))

    shelltools.system("gunzip -v {}/usr/share/dict/cracklib-words.gz".format(get.installDIR()))
    shelltools.system("ln -v -sf cracklib-words {}/usr/share/dict/words".format(get.installDIR()))
    shelltools.system("echo $(hostname) >>      {}/usr/share/dict/cracklib-extra-words".format(get.installDIR()))
    shelltools.system("install -v -m755 -d      {}/lib/cracklib".format(get.installDIR()))

    # Create dictionary files
    shelltools.system("create-cracklib-dict     {0}/usr/share/dict/cracklib-words \
                        {0}/usr/share/cracklib/pw_dict".format(get.installDIR()))

    inarytools.domo("po/tr.po","tr","cracklib.mo")
    inarytools.dodoc("ChangeLog", "README*", "NEWS", "COPYING.LIB", "AUTHORS")

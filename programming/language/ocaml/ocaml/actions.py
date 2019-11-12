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
    #shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer", ""))
    #shelltools.export("LDFLAGS", get.LDFLAGS())

    autotools.rawConfigure("-prefix /usr \
                            -bindir /usr/bin \
                            -libdir /usr/lib/ocaml \
                            -mandir /usr/share/man \
                            --with-pthread")

def build():
    autotools.make("-j1 world")
    autotools.make("-j1 opt")
    autotools.make("-j1 opt.opt")

def install():
    autotools.rawInstall("BINDIR=%(install)s/usr/bin \
                          LIBDIR=%(install)s/usr/lib/ocaml \
                          MANDIR=%(install)s/usr/share/man" \
                          % { "install": get.installDIR()})

    inarytools.dodoc("Changes", "LICENSE", "README*")


    ''' autotools.rawInstall("-C emacs \
                        BINDIR=%(install)s/usr/bin \
                        EMACSDIR=%(install)s/usr/share/emacs/site-lisp"
                        % { "install": get.installDIR()})
    '''
    # Remove rpaths from stublibs .so files
    # shelltools.system("chrpath --delete %s/usr/lib/ocaml/stublibs/*.so" % get.installDIR())
     

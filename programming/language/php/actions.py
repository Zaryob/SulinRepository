#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():

    common_options = "--sysconfdir=/etc \
            --without-pear               \
            --enable-fpm                 \
            --with-fpm-user=apache       \
            --with-fpm-group=apache      \
            --with-config-file-path=/etc \
            --with-zlib                  \
            --enable-bcmath              \
            --with-bz2                   \
            --enable-calendar            \
            --enable-dba=shared          \
            --with-gdbm                  \
            --with-gmp                   \
            --enable-ftp                 \
            --with-gettext               \
            --enable-mbstring            \
            --disable-mbregex            \
            --with-readline "

    autotools.configure(common_options)

def build():
    shelltools.export("LC_ALL", "en_US.UTF-8")
    autotools.make()


#def check():
#    shelltools.cd("apache")
#    autotools.make("test")

def install():
    autotools.rawInstall("INSTALL_ROOT=\"{}\"".format(get.installDIR()))

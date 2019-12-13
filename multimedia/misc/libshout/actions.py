#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-theora \
                         --enable-speex")
    inarytools.dosed("src/tls.c", 'SSLeay_add_all_algorithms','OpenSSL_add_all_algorithms')

def build():
    autotools.make()

def install():
    autotools.install()

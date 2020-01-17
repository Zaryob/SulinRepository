#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools


def setup():
    autotools.configure("PYTHON=python3 \
                         --with-package-name='Sulin gst-libav package' \
                         --with-package-origin='http://www.github.com/SulinOS/' \
                         --enable-ffmpeg")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("README","NEWS","ChangeLog")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools

def setup():
    mesontools.meson_configure("-DBUILD_RARPD=true \
                                -DBUILD_HTML_MANS=false \
                    			-DBUILD_MANS=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import rubymodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    rubymodules.gem_build()

def install():
    rubymodules.gem_install("   --no-user-install \
                                --ignore-dependencies \
                                --no-document ")

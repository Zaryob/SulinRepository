#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def build():
    shelltools.system("""perl Build.PL installdirs=vendor create_packlist=0
                                     LC_ALL=en_US.UTF-8 perl Build""")

def install():
    shelltools.system(""" perl Build destdir="{}" install""".format(get.installDIR()))
    shelltools.system("""find "{}" -name .packlist -o -name perllocal.pod -delete""".format(get.installDIR()))


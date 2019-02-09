#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

binFiles = ["nasm", "ndisasm"]
rdoffFiles = ["ldrdf", "rdf2bin", "rdf2ihx", "rdfdump", "rdflib", "rdx"]

def setup():
    autotools.configure()

def build():
    autotools.make("all")
    autotools.make("rdf")

def install():
    for i in rdoffFiles:
        binFiles.append("rdoff/%s" % i)

    for i in binFiles:
        inarytools.dobin(i)

    inarytools.dosym("rdf2bin", "/usr/bin/rdf2com")

    inarytools.doman("nasm.1", "ndisasm.1")
    inarytools.dodoc("AUTHORS", "CHANGES", "ChangeLog", "README", "TODO", "doc/nasmdoc.*")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="."


def install():
    for version in ["4.1.2"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/*.mod")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/docbook.cat")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.1.2/ent/*.ent")
        
    for version in ["4.2"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/*.mod")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/docbook.cat")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.2/ent/*.ent")
        
    for version in ["4.3"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/*.mod")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/docbook.cat")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.3/ent/*.ent")
        
    for version in ["4.4"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/*.mod")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/docbook.cat")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.4/ent/*.ent")
        
    for version in ["4.5"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "*.mod")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "docbook.cat")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "ent/*.ent")
        
    for version in ["5.0"]:
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/dtd" % version, "docbook-5.0/dtd/*.dtd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/rng" % version, "docbook-5.0/rng/*.rng")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/rng" % version, "docbook-5.0/rng/*.rnc")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/xsd" % version, "docbook-5.0/xsd/*.xsd")
        inarytools.insinto("/usr/share/xml/docbook/xml-dtd-%s/sch" % version, "docbook-5.0/sch/*.sch")
    
    inarytools.dodoc("ChangeLog", "README")

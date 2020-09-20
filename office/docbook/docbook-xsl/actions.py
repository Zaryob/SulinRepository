
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def install():
    ver="1.79.2"
    shelltools.system("install -v -m755 -d {}/usr/share/xml/docbook/xsl-stylesheets-{}".format(get.installDIR(),ver))
    shelltools.system("cp -v -R assembly common eclipse epub epub3 fo highlighting html \
		htmlhelp javahelp lib manpages params profiling roundtrip \
		template website xhtml xhtml-1_1 xhtml5                                         \
    {}/usr/share/xml/docbook/xsl-stylesheets-{}".format(get.installDIR(),ver))
    shelltools.system("ln -s VERSION {}/usr/share/xml/docbook/xsl-stylesheets-{}/VERSION.xsl".format(get.installDIR(),ver))
    shelltools.system("install -dm755 {}/etc/xml || return 1".format(get.installDIR()))
    shelltools.system("install -v -m644 -D README  {}/usr/share/xml/docbook/xsl-stylesheets-{}/README.txt".format(get.installDIR(),ver))
    shelltools.system("install -v -m644    RELEASE-NOTES* NEWS*  {}/usr/share/xml/docbook/xsl-stylesheets-{}".format(get.installDIR(),ver))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

WorkDir = "apache-ant-%s" % get.srcVERSION()
anthome = "/usr/share/ant"
javadir = "/usr/share/java"

def build():
    shelltools.export("ANT_OPTS", "-Duser.home=%s" % WorkDir)
    shelltools.system("./bootstrap.sh")


def install():
#    inarytools.insinto("/etc/ant/", "%s/etc/*" % WorkDir)
#    inarytools.remove("/etc/ant/ant-bootstrap.jar")
    inarytools.insinto("/usr/share/java/ant/", "lib/*")
    inarytools.insinto("/usr/share/java/", "lib/optional/junit-4.12.jar", "junit.jar")
    inarytools.insinto("/usr/share/java/", "lib/optional/hamcrest-core-1.3.jar", "hamcrest.jar")
    inarytools.insinto("/usr/share/ant/lib/", "bootstrap/lib/*")
    inarytools.insinto("/usr/share/ant/bin/", "bootstrap/bin/*")


    for binsym in ["ant", "antRun", "antRun.pl", "complete-ant-cmd.pl", "runant.pl", "runant.py"]:
            inarytools.dosym("/usr/share/ant/bin/%s" % binsym , "/usr/bin/%s" % binsym)

    inarytools.insinto("/usr/share/doc/ant/", "manual/*") #for and-docs
    inarytools.dodoc("KEYS", "NOTICE", "README", "WHATSNEW", "LICENSE")

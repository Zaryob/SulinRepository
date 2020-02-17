#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("ALT_PARALLEL_COMPILE_JOBS", get.makeJOBS())
shelltools.export("HOTSPOT_BUILD_JOBS", get.makeJOBS())
shelltools.export("LC_ALL", "C")
shelltools.export("CFLAGS","-Wno-error=deprecated-declarations -Wno-error=stringop-overflow= -Wno-error=return-type -Wno-error=cpp -fno-lifetime-dse -fno-delete-null-pointer-checks")

def setup():
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    shelltools.system("chmod +x ./configure")
    autotools.rawConfigure("--with-milestone=\"fcs\" \
    --enable-unlimited-crypto \
    --with-zlib=system")

def build():
    shelltools.system("make JOBS=5")

def check():
    autotools.make("check -k")

def install():
    jvmdir="/usr/lib/jvm/java-8-openjdk"

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "README", "NEWS")

    #cd main output directory
    shelltools.cd("openjdk.build")

    #---- install openjdk8-doc
    inarytools.insinto("/usr/share/doc/openjdk8-doc", "docs/*")

    #install openjdk8-src
    inarytools.insinto(jvmdir, "images/j2sdk-image/src.zip")

    #---- instal jdk8-openjdk
    for d in ["include","lib","bin"]:
        inarytools.insinto(jvmdir, "images/j2sdk-image/%s" % d)
    #install openjdk8-src
    # inarytools.insinto(jvmdir, "images/j2re-image/src.zip")

    for f in shelltools.ls("%s/usr/lib/jvm/java-8-openjdk/bin/" % get.installDIR()):
        if not f in ["java", "java-rmi.cgi", "keytool", "orbd",
                     "pack200", "policytool", "rmid", "rmiregistry",
                     "servertool", "tnameserv", "unpack200"]:
            inarytools.dosym("/usr/lib/jvm/java-8-openjdk/bin/%s" % f, "/usr/bin/%s" % f)

    #install man pages
    inarytools.doman("images/j2sdk-image/man/man1/*")
    inarytools.insinto("/usr/share/man/ja/man1", "images/j2sdk-image/man/ja_JP.UTF-8/man1/*.1")
    inarytools.insinto("/usr/share/applications", "../jconsole.desktop")
    shelltools.system("chmod go+r %s%s/lib/sa-jdi.jar" %(get.installDIR(), jvmdir))

    #---- instal jre8-openjdk
    inarytools.insinto("%s/jre/bin" % jvmdir , "images/j2sdk-image/jre/bin/*")
    #inarytools.insinto("%s/jre/lib/amd64" % jvmdir , "j2sdk-image/jre/lib/amd64/xawt")
    for binfile in shelltools.ls("images/j2sdk-image/jre/bin"):
        try:
            inarytools.dosym("%s/jre/bin/%s" % (jvmdir, binfile), "/usr/bin/%s" % binfile)
        except:
            pass

    inarytools.insinto("/usr/share/applications", "../policytool.desktop")

    for size in [16, 24, 32, 48]:
        fullsize = "%dx%d" % ((size, ) * 2)
        inarytools.insinto("/usr/share/icons/hicolor/%s/apps/" % fullsize, "../openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon%d.png" % size, "java.png")

    #---- install jre8-openjdk-headless
    inarytools.insinto("%s/jre/" % jvmdir , "images/j2sdk-image/jre/lib")
    inarytools.insinto("%s/jre/bin" % jvmdir, "images/j2sdk-image/jre/bin/*")

    # inarytools.rename("%s/jre/lib/fontconfig.Ubuntu.properties.src" % jvmdir , "fontconfig.properties")
    # inarytools.rename("%s/jre/lib/fontconfig.Ubuntu.bfc" % jvmdir , "fontconfig.bfc")
    #inarytools.remove("%s/jre/lib/fontconfig.*.bfc" % jvmdir)
    #inarytools.remove("%s/jre/lib/fontconfig.*.properties.src" % jvmdir)

    inarytools.domove("%s/jre/lib/*.properties*" % jvmdir,"/etc/java-8-openjdk/")

    for propfile in shelltools.ls("%s/etc/java-8-openjdk/" % get.installDIR()):
        inarytools.dosym("/etc/java-8-openjdk/%s" % propfile, "%s/jre/lib/%s" % (jvmdir, propfile))

    inarytools.domove("%s/jre/lib/images/cursors/cursors.properties" % jvmdir,"/etc/java-8-openjdk/cursors/")
    inarytools.dosym("/etc/java-8-openjdk/cursors/cursors.properties", "%s/jre/lib/images/cursors/cursors.properties" % jvmdir)

    inarytools.rename("%s/jre/lib/management/jmxremote.password.template" % jvmdir , "jmxremote.password")
    inarytools.rename("%s/jre/lib/management/snmp.acl.template" % jvmdir , "snmp.acl")

    for f in ["management.properties", "jmxremote.access", "jmxremote.password", "snmp.acl"]:
        inarytools.domove("%s/jre/lib/management/%s" % (jvmdir, f),"/etc/java-8-openjdk/management/")
        inarytools.dosym("/etc/java-8-openjdk/management/%s" % f, "%s/jre/lib/management/%s" % (jvmdir, f))

    for f in ["java.policy","java.security","nss.cfg"]:
        inarytools.domove("%s/jre/lib/security/%s" % (jvmdir, f),"/etc/java-8-openjdk/security/")
        inarytools.dosym("/etc/java-8-openjdk/security/%s" % f, "%s/jre/lib/security/%s" % (jvmdir, f))

    #confs=os.listdir("%s/etc/java-8-openjdk/" % get.installDIR())
    #for i in confs:
        #shelltools.system("chmod 0644 %s/etc/java-8-openjdk/%s" % (get.installDIR, i))

    #inarytools.domove("%s/jre/lib/fontconfig.bfc" % jvmdir,"/etc/java-8-openjdk/")
    inarytools.domove("%s/jre/lib/amd64/jvm.cfg" % jvmdir,"/etc/java-8-openjdk/")
    inarytools.dosym("/etc/java-8-openjdk/jvm.cfg" , "%s/jre/lib/amd64/jvm.cfg" % jvmdir)

    for license in ["LICENSE", "THIRD_PARTY_README", "ASSEMBLY_EXCEPTION"]:
        inarytools.insinto("/usr/share/doc/jre8-openjdk-headless", "images/j2re-image/%s" % license)

    inarytools.remove("%s/jre/lib/security/cacerts" % jvmdir)

    #seems we need to add this symlink into ca-certificates-java package ?
    inarytools.dosym("/etc/ssl/certs/java/cacerts", "%s/jre/lib/security/cacerts" % jvmdir)

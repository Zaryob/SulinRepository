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

def setup():
    shelltools.system('export DISTRIBUTION_PATCHES="patches/fontconfig-paths.diff \
                               patches/openjdk7_nonreparenting-wm.diff\
                               patches/giflib_5.1.diff"')

    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    autotools.rawConfigure("\
                            --disable-tests \
                            --disable-Werror \
                            --with-parallel-jobs=%s \
                            --enable-nss \
                            --with-rhino \
                            --disable-system-kerberos \
                            --disable-system-pcsc \
                            --disable-system-sctp \
                            --enable-bootstrap \
                            --with-jdk-home=/usr/lib/jvm/java-7-openjdk \
                            --with-pkgversion='Sulin build 7.u121_2.6.19' \
                           " % get.makeJOBS().replace("-j", ""))

def build():
    autotools.make()

def check():
    autotools.make("check -k")

def install():
    jvmdir="/usr/lib/jvm/java-7-openjdk"

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "README", "NEWS")

    #cd main output directory
    shelltools.cd("openjdk.build")

    #---- install openjdk7-doc
    inarytools.insinto("/usr/share/doc/openjdk7-doc", "docs/*")

    #install openjdk7-src
    inarytools.insinto(jvmdir, "images/j2sdk-image/src.zip")

    #---- instal jdk7-openjdk
    for d in ["include","lib","bin"]:
        inarytools.insinto(jvmdir, "images/j2sdk-image/%s" % d)
    #install openjdk7-src
    # inarytools.insinto(jvmdir, "images/j2re-image/src.zip")

    for f in shelltools.ls("%s/usr/lib/jvm/java-7-openjdk/bin/" % get.installDIR()):
        if not f in ["java", "java-rmi.cgi", "keytool", "orbd",
                     "pack200", "policytool", "rmid", "rmiregistry",
                     "servertool", "tnameserv", "unpack200"]:
            inarytools.dosym("/usr/lib/jvm/java-7-openjdk/bin/%s" % f, "/usr/bin/%s" % f)

    #install man pages
    inarytools.doman("images/j2sdk-image/man/man1/*")
    inarytools.insinto("/usr/share/man/ja/man1", "images/j2sdk-image/man/ja_JP.UTF-8/man1/*.1")
    inarytools.insinto("/usr/share/applications", "../jconsole.desktop")
    shelltools.system("chmod go+r %s%s/lib/sa-jdi.jar" %(get.installDIR(), jvmdir))

    #---- instal jre7-openjdk
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

    #---- install jre7-openjdk-headless
    inarytools.insinto("%s/jre/" % jvmdir , "images/j2sdk-image/jre/lib")
    inarytools.insinto("%s/jre/bin" % jvmdir, "images/j2sdk-image/jre/bin/*")

    # inarytools.rename("%s/jre/lib/fontconfig.Ubuntu.properties.src" % jvmdir , "fontconfig.properties")
    # inarytools.rename("%s/jre/lib/fontconfig.Ubuntu.bfc" % jvmdir , "fontconfig.bfc")
    #inarytools.remove("%s/jre/lib/fontconfig.*.bfc" % jvmdir)
    #inarytools.remove("%s/jre/lib/fontconfig.*.properties.src" % jvmdir)

    inarytools.domove("%s/jre/lib/*.properties*" % jvmdir,"/etc/java-7-openjdk/")

    for propfile in shelltools.ls("%s/etc/java-7-openjdk/" % get.installDIR()):
        inarytools.dosym("/etc/java-7-openjdk/%s" % propfile, "%s/jre/lib/%s" % (jvmdir, propfile))

    inarytools.domove("%s/jre/lib/images/cursors/cursors.properties" % jvmdir,"/etc/java-7-openjdk/cursors/")
    inarytools.dosym("/etc/java-7-openjdk/cursors/cursors.properties", "%s/jre/lib/images/cursors/cursors.properties" % jvmdir)

    inarytools.rename("%s/jre/lib/management/jmxremote.password.template" % jvmdir , "jmxremote.password")
    inarytools.rename("%s/jre/lib/management/snmp.acl.template" % jvmdir , "snmp.acl")

    for f in ["management.properties", "jmxremote.access", "jmxremote.password", "snmp.acl"]:
        inarytools.domove("%s/jre/lib/management/%s" % (jvmdir, f),"/etc/java-7-openjdk/management/")
        inarytools.dosym("/etc/java-7-openjdk/management/%s" % f, "%s/jre/lib/management/%s" % (jvmdir, f))

    for f in ["java.policy","java.security","nss.cfg"]:
        inarytools.domove("%s/jre/lib/security/%s" % (jvmdir, f),"/etc/java-7-openjdk/security/")
        inarytools.dosym("/etc/java-7-openjdk/security/%s" % f, "%s/jre/lib/security/%s" % (jvmdir, f))

    #confs=os.listdir("%s/etc/java-7-openjdk/" % get.installDIR())
    #for i in confs:
        #shelltools.system("chmod 0644 %s/etc/java-7-openjdk/%s" % (get.installDIR, i))

    #inarytools.domove("%s/jre/lib/fontconfig.bfc" % jvmdir,"/etc/java-7-openjdk/")
    inarytools.domove("%s/jre/lib/amd64/jvm.cfg" % jvmdir,"/etc/java-7-openjdk/")
    inarytools.dosym("/etc/java-7-openjdk/jvm.cfg" , "%s/jre/lib/amd64/jvm.cfg" % jvmdir)

    for license in ["LICENSE", "THIRD_PARTY_README", "ASSEMBLY_EXCEPTION"]:
        inarytools.insinto("/usr/share/doc/jre7-openjdk-headless", "images/j2re-image/%s" % license)

    inarytools.remove("%s/jre/lib/security/cacerts" % jvmdir)

    #seems we need to add this symlink into ca-certificates-java package ?
    inarytools.dosym("/etc/ssl/certs/java/cacerts", "%s/jre/lib/security/cacerts" % jvmdir)

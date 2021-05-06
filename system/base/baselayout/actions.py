# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def install():
    for i in {"/bin", "/sbin", "/lib", "/lib32","/data/srv","/kernel","/kernel/boot",
              "/etc","/tmp","/data/misc","/data","/data/user","/data/app","/data/user/root",
              "/tmp", "/usr", "/usr/bin","/kernel/modules","/data/app/system",
              "/usr/lib", "/usr/lib32", "/usr/libexec", "/usr/share","/kernel/firmware",
              "/run", "/usr/local", "/usr/local/bin", "/usr/local/lib", "/usr/local/libexec",
              "/usr/local/lib32","/data/log","/data/lock","/var","/data/srv/www","/usr/src"}:
        inarytools.dodir(i)

    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))


# SulinOS GNU/Linux filesystem architecture (like android and LFS)
#
#    /data/
#        ->app          = Userspace application directory
#            ->system   = Userspace optional system application
#        ->data         = Infinitive loop directory ( /data linked here )
#        ->media        = userspace mounted volumes ( /var/run/mount linked here )
#        ->user         = User's home directory
#            ->root     = The root home ( /root linked here )
#        ->misc         = Is an unused directory
#        ->tmp          = Temp directory ( linked /tmp )
#        ->srv          = Served directory
#            ->www      = Web directory
#        ->log          = System logs
#        ->lock         = System locks
#
#    /kernel/
#         ->boot        = Linux kernel files ( /boot linked here )
#         ->modules     = Linux kernel module files ( /lib/modules linked here )
#         ->firmware    = Linux kernel firmware files ( /lib/firmware linked here )
#         ->dev         = The dev directory ( /dev linked here )
#         ->sys         = The sys directory ( /sys linked here )
#         ->proc        = The proc directory ( /proc linked here )
#
#    /run => /var/run
#

    inarytools.dosym("../run", "/var/run")
    inarytools.dosym("../tmp", "/var/tmp")
    inarytools.dosym("data/user/root", "/root")
    inarytools.dosym("../tmp/", "/data/tmp")
    inarytools.dosym("../data", "/data/data")
    inarytools.dosym("../data/log", "/var/log")
    inarytools.dosym("../data/srv/www", "/var/www")
    inarytools.dosym("../data/lock", "/var/lock")
    inarytools.dosym("../run/media", "/data/media")

    inarytools.dosym("../dev","/kernel/dev")
    inarytools.dosym("../sys","/kernel/sys")
    inarytools.dosym("../proc","/kernel/proc")
    inarytools.dosym("kernel/boot", "/boot")
    inarytools.dosym("../kernel/modules", "/lib/modules")
    inarytools.dosym("../kernel/firmware", "/lib/firmware")

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        inarytools.dodir("/lib32")
        inarytools.dodir("/usr/lib32")
        inarytools.dodir("/usr/local/lib32")

        # Hack for binary blobs built on multi-lib systems
        inarytools.dosym("lib", "/lib64")
        inarytools.dosym("lib32", "/libx32")
        inarytools.dosym("lib", "/usr/lib64")
        inarytools.dosym("../lib", "/usr/lib/x86_64-linux-gnu")
        inarytools.dosym("../lib32", "/usr/lib32/i686-linux-gnu")
        inarytools.dosym("lib32", "/usr/libx32")
        inarytools.dosym("lib", "/usr/local/lib64")
        inarytools.dosym("lib32", "/usr/local/libx32")
        inarytools.dosym("../lib", "/usr/local/lib/x86_64-linux-gnu")
        inarytools.dosym("../lib32", "/usr/local/lib32/i686-linux-gnu")

    # Adjust permissions
    shelltools.system("chmod 755 -R {}/".format(get.installDIR()))
    shelltools.chmod("{}/tmp".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/usr/share/baselayout/shadow".format(get.installDIR()), 0o600)
    shelltools.chmod("{}/data/user/root".format(get.installDIR()), 0o600)


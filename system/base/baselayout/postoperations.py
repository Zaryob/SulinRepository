#!/usr/bin/env python3

import os
import grp
import pwd
import shutil


def postInstall():
    # We don't want to overwrite an existing file during upgrade
    os.mkdir("/etc/bash/")
    os.mkdir("/etc/bashrc.d/")
    specialFiles = ["passwd", "locale.conf", "group", "fstab", "ld.so.conf", "resolv.conf","bash/bashrc"]
    for rcfile in os.listdir("/usr/share/baselayout/bash/bashrc.d"):
        specialFiles.append("bash/bashrc.d/"+rcfile)


    for specialFile in specialFiles:
        if not os.path.exists("/etc/%s" % specialFile):
            os.chmod("/usr/share/baselayout/{}".format(specialFile),0o755)
            shutil.copy("/usr/share/baselayout/{}".format(specialFile), "/etc{}".format(specialFile))
    
    
    shutil.copy("/usr/share/baselayout/inittab.openrc", "/etc/inittab")
    shutil.copy("/usr/share/baselayout/shadow", "/etc/shadow")
    shutil.copy("/usr/share/baselayout/index.theme", "/usr/share/icons/hicolor/index.theme")
    os.chmod("/usr/share/icons/hicolor/index.theme",0o755)


    # We should only install empty files if these files don't already exist.
    if not os.path.exists("/var/log/lastlog"):
        os.system("/bin/touch /var/log/lastlog")

    if not os.path.exists("/run/utmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /run/utmp")

    if not os.path.exists("/var/log/wtmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/log/wtmp")


    # Create /root if not exists
    if not os.path.exists("/data/user/root/"):
        os.chown("/data/user/root/", 0, 0)
        os.chmod("/data/user/root/", 0o700)


    # Save user defined DNS
    if not os.access("/etc/resolv.default.conf", os.R_OK):
        os.system("cp /etc/resolv.conf /etc/resolv.default.conf")

    # Fix permissions of /var/lock folder
    os.chown("/var/lock", 0, 54)
    os.chmod("/var/lock", 0o775)
    

def postRemove():
    pass

def preRemove():
    pass

#!/usr/bin/env python3

import os

def create_dir(name):
    if os.path.exists(name)==False:
        os.system("mkdir -p "+name)
def copy_file(source,target,perm):
	os.system("cp -prf '"+source+"' '"+target+"'")
	os.chmod(target,perm)

def postInstall():
    """base config"""
    create_dir("/etc/bash/")
    create_dir("/etc/bash/bashrc.d")
    create_dir("/usr/share/icons/hicolor/")
    specialFiles = ["passwd", "locale.conf", "group", "fstab", "ld.so.conf", "resolv.conf"]

    for specialFile in specialFiles:
        copy_file("/usr/share/baselayout/{}".format(specialFile), "/etc/{}".format(specialFile),0o755)

    
    
    copy_file("/usr/share/baselayout/inittab.openrc", "/etc/inittab",0o700)
    copy_file("/usr/share/baselayout/bash/bashrc","/etc/bash/bashrc",0o755)
    for i in os.listdir("/usr/share/baselayout/bash/bashrc.d"):
	    copy_file("/usr/share/baselayout/bash/bashrc.d/"+i, "/etc/bash/bashrc.d/"+i,0o755)
    copy_file("/usr/share/baselayout/shadow", "/etc/shadow",0o700)
    copy_file("/usr/share/baselayout/index.theme", "/usr/share/icons/hicolor/index.theme",0o755)
    os.chmod("/usr/share/icons/hicolor/index.theme",0o755)


    # We should only install empty files if these files don't already exist.
    if not os.path.exists("/var/log/lastlog"):
        os.system("/bin/touch /var/log/lastlog")


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

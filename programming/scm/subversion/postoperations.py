#!/usr/bin/env python3

import os

def postInstall():
    os.system("/bin/mkdir -p /var/svn/conf")
    os.system("/usr/bin/svnadmin create /var/svn/repos")

    os.system("/bin/chmod -R 774 /var/svn/repos")
    os.system("/bin/chmod 775 /var/svn/repos")

    os.system("/bin/chown -R svn:svn /var/svn")

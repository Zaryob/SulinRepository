import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.chmod("/sbin/unix_chkpwd", 0o4755)

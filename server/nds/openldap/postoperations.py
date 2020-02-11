#!/usr/bin/env python3

import os
import pwd
import grp

def postInstall():
    os.system("groupadd -g 83 ldap")
    os.system("useradd  -c \"OpenLDAP Daemon Owner\" \
               -d /var/lib/openldap -u 83 \
               -g ldap -s /bin/false ldap")
    os.system("/bin/chown ldap:ldap /run/openldap")
    os.system("/bin/chown root:ldap /etc/openldap/slapd.conf")
    os.system("/bin/chown root:ldap /etc/openldap/slapd.conf.default")
    os.system("/bin/chmod 0755 /run/openldap")
    os.system("/bin/chmod 0640 /etc/openldap/slapd.conf")
    os.system("/bin/chmod 0640 /etc/openldap/slapd.conf.default")

def postRemove():
    pass

def preRemove():
    pass

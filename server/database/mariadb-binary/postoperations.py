#!/usr/bin/env python3

import os, re
import shutil

OUR_ID = 794
OUR_NAME = "mysql"
OUR_DESC = "mysql"

DATADIR = "/var/lib/mysql"
DATADIRMODE = 0o755

def postInstall():
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/mysql -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
    except:
        pass

        # Create the database
    os.system("/bin/chown -R mysql:mysql %s" % DATADIR)
    os.system("/bin/chown -R mysql:mysql /var/log/mysqld.log")
    os.system("/usr/bin/mysql_install_db --user=mysql --datadir=/var/lib/mysql --basedir=/usr --force")
    os.system("/usr/bin/mysql_upgrade --force")

    magic=open("/etc/magic", "a")
    magic.write(
"""0       beshort           0xfe01        MySQL table definition file
>2      byte            x               Version %d
0       belong&0xffffff00 0xfefe0700    MySQL MyISAM index file
>3      byte            x               Version %d
0       belong&0xffffff00 0xfefe0800    MySQL MyISAM compressed data file
>3      byte            x               Version %d
0       belong&0xffffff00 0xfefe0900    MySQL Maria index file
>3      byte            x               Version %d
0       belong&0xffffff00 0xfefe0A00    MySQL Maria compressed data file
>3      byte            x               Version %d
0       belong&0xffffff00 0xfefe0500    MySQL ISAM index file
>3      byte            x               Version %d
0       belong&0xffffff00 0xfefe0600    MySQL ISAM compressed data file
>3      byte            x               Version %d
0       string           \376bin        MySQL replication log
0       belong&0xffffff00 0xfefe0b00
>4      string          MARIALOG        MySQL Maria transaction log file
>>3     byte            x               Version %d
0       belong&0xffffff00 0xfefe0c00
>4      string          MACF            MySQL Maria control file
>>3     byte            x               Version %d
""")
    magic.close()
    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)


def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass

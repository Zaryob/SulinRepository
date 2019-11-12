#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import perlmodules
from inary.actionsapi import get

NGINX_HOME = '/var/lib/nginx'
NGINX_PID  = '/run/nginx.pid'
NGINX_LOCK = '/run/nginx.lock'
NGINX_CONF = '/etc/nginx/nginx.conf'
NGINX_HTML = '/var/www/nginx'

LOG_DIR    = '/var/log/nginx'
ERROR_LOG    = '%s/error.log' % LOG_DIR
ACCESS_LOG   = '%s/access.log' % LOG_DIR

def setup():
    autotools.rawConfigure("--user=nginx \
                            --group=nginx \
                            --prefix=%(html)s \
                            --sbin-path=/usr/sbin/nginx \
                            --conf-path=%(conf)s \
                            --pid-path=%(pid)s \
                            --lock-path=%(lock)s \
                            --error-log-path=%(error)s \
                            --http-log-path=%(access)s \
                            --http-client-body-temp-path=%(home)s/client_body \
                            --http-proxy-temp-path=%(home)s/proxy \
                            --http-fastcgi-temp-path=%(home)s/fastcgi \
                            --with-compat \
                            --with-debug \
                            --with-file-aio \
                            --with-http_addition_module \
                            --with-http_auth_request_module \
                            --with-http_dav_module \
                            --with-http_degradation_module \
                            --with-http_flv_module \
                            --with-http_geoip_module \
                            --with-http_gunzip_module \
                            --with-http_gzip_static_module \
                            --with-http_mp4_module \
                            --with-http_realip_module \
                            --with-http_secure_link_module \
                            --with-http_slice_module \
                            --with-http_ssl_module \
                            --with-http_stub_status_module \
                            --with-http_sub_module \
                            --with-http_v2_module \
                            --with-mail \
                            --with-mail_ssl_module \
                            --with-pcre-jit \
                            --with-stream \
                            --with-stream_geoip_module \
                            --with-stream_realip_module \
                            --with-stream_ssl_module \
                            --with-stream_ssl_preread_module  \
                            --with-threads" % {'html': NGINX_HTML, \
                                                       'conf': NGINX_CONF, \
                                                       'pid': NGINX_PID, \
                                                       'lock': NGINX_LOCK, \
                                                       'error': ERROR_LOG, \
                                                       'access': ACCESS_LOG, \
                                                       'home': NGINX_HOME})


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # For 3rd-party configuration files
    inarytools.dodir("/etc/nginx/conf.d")

    # Add log dir and touch them :) Nginx needs pre-defined *.log files
    inarytools.dodir(LOG_DIR)
    shelltools.touch("%s%s" % (get.installDIR(), ERROR_LOG))
    shelltools.touch("%s%s" % (get.installDIR(), ACCESS_LOG))

    inarytools.dodir(NGINX_HOME + "/client_body")
    inarytools.dodir(NGINX_HOME + "/fastcgi")
    inarytools.dodir(NGINX_HOME + "/proxy")

    inarytools.dodoc("README", "LICENSE")
    inarytools.remove("/etc/nginx/mime.types")

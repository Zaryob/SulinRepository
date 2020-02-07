#!/usr/bin/env python3

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        # Trailing slash is important since it is used with dosed.
        encodingsDir = "/usr/share/fonts/encodings/"
        # Font scaling
        os.chdir("{}large".format(encodingsDir))
        os.system("/usr/bin/mkfontscale -b -s -l -n -r -p {}large -e . .".format(encodingsDir))

        os.chdir("{}".format(encodingsDir))
        os.system("/usr/bin/mkfontscale -b -s -l -n -r -p {} -e . -e large .".format(encodingsDir))
        os.system("/usr/bin/mkfontdir -n -e {0} -e {0}large .".format(encodingsDir))
        os.system("sed -i 's|{}||' encodings.dir ".format(encodingsDir))
        #fontdir generate
        os.system("/usr/bin/mkfontdir /usr/share/fonts/*")

    except:
        pass

def postRemove():
    pass

def preRemove():
    pass

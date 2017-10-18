# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-18T03:12:50+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: main.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-18T03:27:08+02:00

import time

import daemon

if __name__ == "__main__":
    with daemon.DaemonContext():
        fd = open("/tmp/myTrashFile", 'w', 0)
        while 42:
            fd.write("Answer is 42\n")
            time.sleep(1)

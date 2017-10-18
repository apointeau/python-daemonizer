# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-18T01:41:23+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: DaemonContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-18T03:16:37+02:00

import os, sys, atexit

class DaemonContext:
    """

     following the PEP 3143

    """
    is_open = False

    def __init__(self, stdin=None, stdout=None, stderr=None,
                working_directory='/', chroot_directory=None,
                uid=os.getuid(), gid=os.getgid(), files_preserve=None,
                umask=0, pidfile=None,
                detach_process=True, signal_map=None, prevent_core=True):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.working_directory = working_directory
        self.chroot_directory = chroot_directory
        self.uid = uid
        self.gid = gid
        self.files_preserve = files_preserve
        self.umask = umask
        self.pidfile = pidfile
        self.detach_process = detach_process
        self.signal_map = signal_map
        self.prevent_core = prevent_core


    def __enter__(self):
        self.open()
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()


    def open(self):
        if self.is_open:
            return None
        self._set_system_limits()
        if self.chroot_directory:
            os.chroot(self.chroot)
        os.setuid(self.uid)
        os.setgid(self.gid)
        self._close_all_file_descriptors()
        os.chdir(self.working_directory)
        os.umask(self.umask)
        if self.detach_process and os.fork():
            sys.exit(0)
        self._set_signal_handlers()
        self.is_open = True
        return None


    def close(self):
        if not self.is_open:
            return None
        self.is_open = False
        return None


    def _set_system_limits(self):
        pass


    def _close_all_file_descriptors(self):
        pass


    def _set_signal_handlers(self):
        pass

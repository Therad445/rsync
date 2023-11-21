# rsync.py

import subprocess


class Rsync:
    def __init__(self, code, source_dir, dest_dir):
        self.code = code
        self.source_dir = source_dir
        self.dest_dir = dest_dir

    def run(self):
        rsync_cmd = ['rsync', self.code, '--delete', self.source_dir, self.dest_dir]
        subprocess.run(rsync_cmd, check=True)

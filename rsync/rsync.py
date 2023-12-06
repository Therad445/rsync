# rsync.py

import subprocess


class Rsync:
    def __init__(self, code, source_dir, dest_dir, user, ip, port):
        print(user)
        print(ip)
        self.code = code
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        if user != "":
            self.user = str(user) + "@"
        else:
            self.user = user
        if ip != "":
            self.ip = str(ip) + ":~"
        else:
            self.ip = ip
        self.port = port

    def run(self):
        rsync_cmd = ['sudo', 'rsync',self.code, self.source_dir, self.user + self.ip + self.dest_dir]
        print(rsync_cmd)
        subprocess.run(rsync_cmd, check=True)


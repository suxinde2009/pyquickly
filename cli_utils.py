import subprocess

def exec_cmd(cmd):
    return subprocess.run(cmd, shell=False, check=True)

def exec_cmd_line(cmd_line):
    cmd = cmd_line.split(" ")
    return exec_cmd(cmd)
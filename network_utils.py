import subprocess

def check_network_available():
    ret = subprocess.run("ping baidu.com -n 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(ret.returncode)
    return True if ret.returncode == 0 else False
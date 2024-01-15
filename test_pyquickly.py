import pyquickly
import file_utils
import network_utils
import cli_utils

import time_utils
import collections_utils

def test_break():
    print("\n")

def test_network():
    test_break()
    print(network_utils.check_network_available())

    test_break()

def test_file():
    test_break()
    


    test_break()

def test_cli():
    test_break()

    cmd_line = "ffmpeg -h"
    cli_utils.exec_cmd_line(cmd_line)

    cmd = ["ffmpeg", "-h"]
    cli_utils.exec_cmd(cmd)


    test_break()


def test_time():
    test_break()

    t = time_utils.get_web_server_time()
    print(t)

    test_break()

def test_collections_utils():
    test_break()

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(collections_utils.RandomPickItemsFromArray(arr, 5))

    test_break()

def test_start():

    test_network()
    test_cli()
    test_time()
    test_collections_utils()
#---------------------
test_start()





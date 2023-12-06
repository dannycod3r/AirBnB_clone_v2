#!/usr/bin/env python3
"""Module contains function that compresses webstatic folder
"""
from datetime import date
from time import strftime
from fabric.api import local


def do_pack():
    """Function that compresses web_static folder"""
    filename_datetime = strftime("%Y%m%d%H%M%S")

    try:
        local('mkdir versions')
        command = "tar -czvf "
        compressed = "versions/web_static_{}.tgz "
        target = "web_static/"
        local('{}{}{}'.format(command,compressed,target))

        return "{}".format(compressed)

    except Exception as e:
        return None

#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'web_static_' + time + '.' + 'tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))
    if result is not None:
        return archive
    else:
        return None

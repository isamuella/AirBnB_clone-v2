#!/usr/bin/python3
"""Fabric script to deploy web static files to servers"""

from fabric.api import env, put, run
import os

env.hosts = ['44.203.2.87', '3.83.161.239']

def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = f"/data/web_static/releases/{no_ext}"

        # Upload the archive to /tmp/
        put(archive_path, "/tmp/")

        # Create release folder
        run(f"mkdir -p {release_path}")

        # Uncompress the archive
        run(f"tar -xzf /tmp/{file_name} -C {release_path}")

        # Move contents from the subfolder to the release folder
        run(f"mv {release_path}/web_static/* {release_path}/")

        # Delete the now-empty web_static folder
        run(f"rm -rf {release_path}/web_static")

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
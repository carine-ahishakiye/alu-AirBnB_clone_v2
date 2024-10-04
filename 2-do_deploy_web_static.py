#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabric.api import env, put, run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: False if the file doesn't exist or an error occurs, True otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    base_name = file_name.split(".")[0]
    release_path = f"/data/web_static/releases/{base_name}"

    # Upload the archive to /tmp/ directory on the web server
    if put(archive_path, f"/tmp/{file_name}").failed:
        return False

    # Create the release directory
    if run(f"rm -rf {release_path}/").failed:
        return False
    if run(f"mkdir -p {release_path}/").failed:
        return False

    # Extract the archive to the release directory
    if run(f"tar -xzf /tmp/{file_name} -C {release_path}/").failed:
        return False

    # Delete the archive from the /tmp/ directory
    if run(f"rm /tmp/{file_name}").failed:
        return False

    # Move contents of web_static to the release directory
    if run(f"mv {release_path}/web_static/* {release_path}/").failed:
        return False

    # Remove the now empty web_static folder
    if run(f"rm -rf {release_path}/web_static").failed:
        return False

    # Delete the current symbolic link and create a new one
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run(f"ln -s {release_path}/ /data/web_static/current").failed:
        return False

    return True

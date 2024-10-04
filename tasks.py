import os
import tarfile
from datetime import datetime
from invoke import task

@task(name="do_pack")  # use underscores for task name
def do_pack(c):
    """Creates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Define the path to the web_static folder
    web_static_path = "web_static"
    # Get the current timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Define the archive name
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Create the .tgz archive
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(web_static_path, arcname=os.path.basename(web_static_path))

    return archive_name

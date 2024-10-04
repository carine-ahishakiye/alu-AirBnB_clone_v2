from fabric import task
import os
from datetime import datetime

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Define the path to the web_static folder
    web_static_path = "web_static"
    # Get the current timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Define the archive name
    archive_name = f"versions/web_static_{timestamp}.tgz"

    try:
        # Create the .tgz archive
        c.run(f"tar -cvzf {archive_name} {web_static_path}")
        print(f"Packing web_static to {archive_name}")
        return archive_name
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None

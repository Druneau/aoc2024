import tempfile
import os
import subprocess


def write_and_open_in_nvim(data):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file_name = temp_file.name
        # Write data to the temporary file
        if isinstance(data, str):
            temp_file.write(data.encode())
        elif isinstance(data, list):
            temp_file.write("\n".join(map(str, data)).encode())
        elif isinstance(data, dict):
            for key, value in data.items():
                temp_file.write(f"{key}: {value}\n".encode())

    # Open the file in vim
    subprocess.run(["/usr/bin/nvim", temp_file_name])

    # Optionally, delete the temp file after editing
    os.remove(temp_file_name)

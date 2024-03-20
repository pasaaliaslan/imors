import os

from django.core.files import File


def upload(file: File, filepath: str) -> None:
    if file is None:
        raise ValueError("Cannot upload an empty file")

    # Ensure the directory structure exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Open the file in write mode, which will create the file if it doesn't exist
    with open(filepath, "w") as f:
        pass  # You can write any initial content here if needed

    # Open the temporary uploaded file and write its content to the destination file
    with file.open() as temp_file:
        with open(filepath, "ab") as f:
            for chunk in temp_file.chunks():
                f.write(chunk)


def download(filepath: str) -> bytes:
    pass

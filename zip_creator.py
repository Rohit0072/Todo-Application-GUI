import zipfile
import pathlib

def make_archive(filepaths, dest_dir, filename):
    dest_path = pathlib.Path(dest_dir, filename + ".zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["a.txt", "b.txt"], dest_dir="file", filename='zero')
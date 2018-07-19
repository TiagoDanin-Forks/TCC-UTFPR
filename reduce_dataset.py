import os
import shutil

for dirpath, dirnames, filenames in os.walk("./"):
    if os.path.basename(dirpath) == "repository":
        absolute_path = os.path.abspath(dirpath)
        shutil.rmtree(absolute_path, ignore_errors=True)

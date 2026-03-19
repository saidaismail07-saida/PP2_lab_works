import shutil
import os

# copy
shutil.copy("sample.txt", "backup.txt")

# delete safely
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
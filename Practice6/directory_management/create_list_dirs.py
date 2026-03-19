import os

# create nested directories
os.makedirs("test_folder/subfolder", exist_ok=True)

# list files
print(os.listdir("test_folder"))
import shutil

# move file
shutil.move("sample.txt", "test_folder/sample.txt")

# copy file
shutil.copy("test_folder/sample.txt", "sample_copy.txt")
import os
folder = "photos"
files = os.listdir(folder)
print(files)
for file in files:
    print(file)

    old_path = os.path.join(folder, file)
    print(old_path)

    new_name = 'test_' + file
    print(new_name)

    new_path = os.path.join(folder, new_name)
    print(new_path)
    
    os.rename(old_path, new_path)
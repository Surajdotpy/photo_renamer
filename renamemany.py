import os
folder = r"E:\pic"
for file in os.listdir(folder):

    if file.startswith('test_'):
        continue
    old_path = os.path.join(folder, file)

    if not os.path.isfile(old_path):
        continue
    
    new_name = 'test' + file
    new_path = os.path.join(folder, new_name)

    if os.path.exists(new_path):
        continue
    os.rename(old_path, new_path)

    print(file, "-",  new_name)





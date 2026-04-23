import os
folder = r"E:\pic"
files = sorted(os.listdir(folder))

count = 1   

for file in files:
    old_path = os.path.join(folder, file)
    if not os.path.isfile(old_path):
        continue
    new_name = f"img-{count}.jpg"
    new_path = os.path.join(folder, new_name)

    if os.path.exists(new_path):
        print("skipping:", new_name)
        continue
    os.rename(old_path, new_path)
    print(file, "-", new_name)
    count += 1


import os

new_dir_path = "./dummy_media"
os.mkdir(new_dir_path)

for i in range(0, 10):
    file_path = new_dir_path + '/' + str(i)+".txt"
    with open(file_path, 'w') as f:
        f.write("")

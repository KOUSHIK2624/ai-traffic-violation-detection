import os
import time

folder = 'outputs'
max_age_seconds = 3600

if os.path.exists(folder):
    now = time.time()
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            if now - os.path.getmtime(file_path) > max_age_seconds:
                os.remove(file_path)
                print(f'Deleted old file: {file_path}')
else:
    print(f'Folder {folder} does not exist.')


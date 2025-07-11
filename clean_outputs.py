import os
import time

OUTPUT_DIR = "outputs"
MAX_FILE_AGE = 60 * 60  # 1 hour

now = time.time()

for filename in os.listdir(OUTPUT_DIR):
    file_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.isfile(file_path):
        if now - os.path.getmtime(file_path) > MAX_FILE_AGE:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

import os
import shutil

def clear_pycache(start_dir="."):
    for root, dirs, files in os.walk(start_dir):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                full_path = os.path.join(root, dir_name)
                print(f"Removing: {full_path}")
                shutil.rmtree(full_path)
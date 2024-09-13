import os
import argparse

def delete_files():
    filenames = ["HS36_BL_img.bin", "HS36_FW_img.bin", "HS36_MINI_D.icm.code"]
    directory = os.getcwd()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in filenames:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":    
    delete_files()

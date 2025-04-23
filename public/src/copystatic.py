import os
import shutil

def copy_directory_contents(src, dst):
    # Check if the destination directory exists, if not create it
    if not os.path.exists(dst):
        os.makedirs(dst)

    # First, clear the destination directory
    for item in os.listdir(dst):
        item_path = os.path.join(dst, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove subdirectory and all its contents
        else:
            os.remove(item_path)  # Remove file

    # Recursively copy the contents of the source directory to the destination
    for item in os.listdir(src):
        src_item_path = os.path.join(src, item)
        dst_item_path = os.path.join(dst, item)

        if os.path.isdir(src_item_path):  # If the item is a directory
            copy_directory_contents(src_item_path, dst_item_path)  # Recursive call
        else:
            shutil.copy(src_item_path, dst_item_path)  # If it's a file, copy it
            print(f"Copied: {src_item_path} to {dst_item_path}")

def main():
    src_directory = "static"
    dst_directory = "public"
    copy_directory_contents(src_directory, dst_directory)

if __name__ == "__main__":
    main()

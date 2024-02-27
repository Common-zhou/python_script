import os
import shutil

def move_files_to_new_folder(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)

            if os.path.isfile(source_file_path):
                dest_file_path = os.path.join(destination_folder, file)
                counter = 1
                while os.path.exists(dest_file_path):
                    file_name, file_extension = os.path.splitext(file)
                    dest_file_path = os.path.join(destination_folder, f"{file_name}({counter}){file_extension}")
                    counter += 1

                shutil.move(source_file_path, dest_file_path)

if __name__ == "__main__":
    source_folder_path = "D:\\test1"

    destination_folder_path = "D:\\test2"

    move_files_to_new_folder(source_folder_path, destination_folder_path)

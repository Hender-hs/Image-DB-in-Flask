from os import walk

def get_especific_file_to_download(file_name: str, UPLOAD_FOLDER: str) -> tuple :


    def getting_current_file_dir() -> list :

        current_dir_files = []
        
        for item in walk(UPLOAD_FOLDER):
            
            dir_files_list = item[2]

            if len(dir_files_list) == 0:
                continue 

            current_dir_files.extend(dir_files_list)

        return current_dir_files
  

    current_dir_files = getting_current_file_dir()

    file_to_download = ''.join(list(filter(lambda item: item.lower() == file_name.lower(), current_dir_files)))


    def find_path_of_file_to_download() -> str :

        path = file_to_download.split('.')[-1]

        return path

    file_path = find_path_of_file_to_download()


    return (file_to_download, file_path)

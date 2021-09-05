from os import listdir

def type_upload_folder_list(type: str, UPLOAD_FOLDER: str):

    try:

        return listdir(f'{UPLOAD_FOLDER}/{type}')

    except FileNotFoundError:

        return 'there is no this file type'
  

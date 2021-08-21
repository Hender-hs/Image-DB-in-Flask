from os import system, path, getcwd

def ziping_files(request_args, UPLOAD_FOLDER):

    file_type = request_args['file_type']

    compression_rate = request_args['compression_rate']
    
    folder_type = file_type

    path_upload_folder = path.join(UPLOAD_FOLDER, folder_type)

    if not path.exists(path_upload_folder):

        return 'this file type does not exists'

    system(f'cd {path_upload_folder} && zip -{compression_rate} all_files.zip *.{file_type} && mv all_files.zip ~/../../../tmp')
    
    return 'successful'

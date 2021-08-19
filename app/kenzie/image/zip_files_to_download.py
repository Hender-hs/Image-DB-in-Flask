from os import system, path, getcwd

def ziping_files(request_args):

    file_type = request_args['file_type']

    compression_rate = request_args['compression_rate']

    folder_type = file_type
    
    if not path.exists(f'files/{folder_type}'):

        return 'this file type does not exists'

    system(f'cd files/{file_type} && zip -{compression_rate} all_files.zip *.{file_type} && mv all_files.zip ~/../../../tmp')
    
    return 'successful'

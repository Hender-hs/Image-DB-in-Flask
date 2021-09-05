from os import makedirs, path, listdir, walk


def getting_request_files_names(request_files: dict) -> list:

    return [request_files[item].filename for item in request_files]



def getting_all_uploaded_files_in_folder(UPLOAD_FOLDER: str) -> set:
     
    all_files = []
     
    for item in list(walk(UPLOAD_FOLDER)):

        all_files.extend(item[2])

    return set(all_files)



def checking_extensions(request_files: dict) -> set:

    return set([request_files[item].filename.split('.')[-1] for item in request_files])



def uploading_files(request_files: dict, UPLOAD_FOLDER: str) -> list :

    
    def saving_files_from_form_in_folder(item_name: str) -> str:

        sent_file = request_files[item_name]

        filename = sent_file.filename

        file_type = filename.split('.')[-1]


        def create_if_not_has_type_folder() -> None:

            if not file_type in listdir(UPLOAD_FOLDER):

                target_path = path.join(UPLOAD_FOLDER, file_type)

                makedirs(target_path)
        
        create_if_not_has_type_folder()
        

        path_type = path.join(UPLOAD_FOLDER, file_type, filename)

        sent_file.save(path_type)

        return filename


    def looping_uploaded_files() -> list :

        return [saving_files_from_form_in_folder(item) for item in request_files]


    return looping_uploaded_files()

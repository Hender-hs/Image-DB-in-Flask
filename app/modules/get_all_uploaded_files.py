from os import walk, listdir

def getting_all_uploaded_files(UPLOAD_FOLDER: str) -> dict :

    walked_files = {}
    
    def creating_a_dict_with_types() -> None :

        directories_type = listdir(UPLOAD_FOLDER) 
        
        for item in directories_type:

            walked_files.setdefault(item, [])

    creating_a_dict_with_types()

    

    def mounting_folder_uploaded_files_dict_response(item: list) -> None :
        
        folder_type_name = item[0].split('/')[-1]

        if (folder_type_name == 'uploaded_files'):
            
            return

        walked_files.get(folder_type_name)
        
        walked_files.update({folder_type_name: item[2]})
            


    def walking_on_upload_folder() -> None :

        print(list(walk(UPLOAD_FOLDER)))

        for item in walk(UPLOAD_FOLDER):

            mounting_folder_uploaded_files_dict_response(item)

    walking_on_upload_folder()


    return walked_files

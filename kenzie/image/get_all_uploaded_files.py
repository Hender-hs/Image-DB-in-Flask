from os import walk, listdir

def getting_all_uploaded_files(UPLOAD_FOLDER):


    walked_files = {}
    
    def creating_a_dict_with_types():

        directories_type = listdir(UPLOAD_FOLDER) 
        
        for item in directories_type:

            walked_files.setdefault(item, [])

    creating_a_dict_with_types()

    

    def setting_files_in_dict(item):
        
        key = item[0].split('/')[-1]

        if (key == 'files'):
            
            return

        prop_value = walked_files.get(key)

        walked_files.update({key: item[2]})
            


    def walking_dir():

        for item in walk(UPLOAD_FOLDER):

            setting_files_in_dict(item)

    walking_dir()


    return walked_files

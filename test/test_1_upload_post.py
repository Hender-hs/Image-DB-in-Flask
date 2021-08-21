from werkzeug.datastructures import FileStorage
from environs import Env
from app import app
import os


env = Env()
env.read_env()

app.testing = True

test_client = app.test_client()

upload_folder = os.environ.get('UPLOAD_FOLDER')

files_folder_test = os.environ.get('FILES_TEST')


def test_upload_response_201_and_storage_file():


    with open(f'{files_folder_test}/kenzie.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')
        
        expected = 201

        if os.path.isfile(os.path.join(upload_folder, file_storage.filename)):
            
            assert response.status_code == expected




def test_upload_response_409_file_already_exists():


    with open(f'{files_folder_test}/kenzie.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')

        expected = 409

        assert response.status_code == expected




def test_upload_response_415_extension_not_allowed():

    
    with open(f'{files_folder_test}/kenzie.bin', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.bin', content_type='application/octet-stream')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')

        expected = 415

        assert response.status_code == expected




def test_upload_reponse_431_file_too_large():

    with open(f'{files_folder_test}/kenzie-large.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie-large.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')

        expected = 413

        assert response.status_code == expected


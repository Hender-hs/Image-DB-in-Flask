from app import app
import os
from werkzeug.datastructures import FileStorage
from environs import Env


env = Env()
env.read_env()

app.testing = True

test_client = app.test_client()

upload_folder = os.environ.get('UPLOAD_FOLDER')


def test_upload_response_201_and_storage_file():


    with open('kenzie.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')
        
        expected = 201

        if os.path.isfile(os.path.join(upload_folder, file_storage.filename)):
            
            assert response.status_code == expected






def test_upload_response_409_file_already_exists():


    with open('kenzie.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file}, content_type='multipart/form-data')

        expected = 409

        assert response.status_code == expected




def test_upload_response_415_extension_not_allowed():

    
    with open('kenzie.bin', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie.bin', content_type='application/octet-stream')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')

        expected = 415

        assert response.status_code == expected




def test_upload_reponse_431_file_too_large():

    with open('kenzie-large.png', 'rb') as file:

        file_storage = FileStorage(stream=file, filename='kenzie-large.png', content_type='image/png')

        response = test_client.post('/upload', data={'file': file_storage}, content_type='multipart/form-data')

        expected = 413

        assert response.status_code == expected


from app import app

import os

app.testing = True

test_client = app.test_client()


def test_make_download_of_zip_file_200():

    response = test_client.get('/download-zip?file_type=png&compression_rate=0')


    def unziping_downloaded_zip():

        os.system('cd /tmp/ && unzip all_files.zip')

        return os.path.isfile('/tmp/kenzie.png')


    assert unziping_downloaded_zip()
 
    assert response.status_code == 200



def test_make_download_without_query_params():

    response = test_client.get('/download-zip?file_type=jpg&compression_rate=0')

    expected = {'msg': 'this file type does not exists'}

    assert response.json == expected

    assert response.status_code == 404


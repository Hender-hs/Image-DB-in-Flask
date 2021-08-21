from app import app

test_client = app.test_client()


def test_make_download_of_a_existing_especific_file_200():

    response = test_client.get('/download/kenzie.png')

    with open('kenzie.png', 'rb') as file:
        
        expected = file.read()

        assert response.data == expected

        assert response.status_code == 200


def test_make_download_of_especific_file_that_does_NOT_exists_404():

    response = test_client.get('/download/kenzie.bin')

    expected = {'msg': 'file does not exists'}

    assert response.json == expected

    assert response.status_code == 404


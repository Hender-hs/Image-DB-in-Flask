from app import app

test_client = app.test_client()


def test_get_all_uploaded_files():

    response = test_client.get('/files')

    expected = {'png': [ 'kenzie.png' ] }

    assert response.json == expected



def test_get_all_uploaded_files_status():

    response = test_client.get('/files')

    expected = 200

    assert response.status_code == expected


from app import app 

test_client = app.test_client()


def test_get_especific_uploaded_type_file():

    response = test_client.get('/files/png')

    expected_json = [ 'kenzie.png' ]

    assert response.json == expected_json

    assert response.status_code == 200



def test_get_especific_NOT_uploaded_type_file():

    response = test_client.get('/files/jpg')

    expected_json = {'msg': 'there is no this file type'}

    assert response.json == expected_json

    assert response.status_code == 404


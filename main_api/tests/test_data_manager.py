from main_api.manager_data import DataManager
from requests import Response


def test_make_request(mocker):
    mock_test_data = Response()
    mock_test_data._content = b"""{
        "slip": {
            "id": 168,
            "advice": "some_text"
        }
    }"""

    mocker.patch('requests.get', return_value=mock_test_data)
    result = DataManager().make_request()

    assert result == {
        "slip": {
            "id": 168,
            "advice": "some_text"
        }
    }


def test_prepare_data():
    test_manager = DataManager()
    test_manager.data = {
        "slip": {
            "id": 168,
            "advice": "some_text"
        }
    }

    result = test_manager.prepare_data()
    assert result == 'some_text'


def test_get_data(mocker):
    mock_test_data = Response()
    mock_test_data._content = b"""{
        "slip": {
            "id": 168,
            "advice": "some_text"
        }
    }"""

    mocker.patch('requests.get', return_value=mock_test_data)
    data = DataManager().get_data()
    assert data == 'some_text'

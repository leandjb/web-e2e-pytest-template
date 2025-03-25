import pytest
import requests
import requests_mock
from src.controller import ApiHandler

api_handler = ApiHandler()
status_codes_for_tests = [400, 401, 402, 404, 500, 501]

@pytest.mark.smoke
def test_mock_get_data_from_api():
    # simulation API call with mock

    with requests_mock.Mocker() as mocker:
        url = 'https://rickandmortyapi.com/api/'

        mocker.get(url,
                   json={'data': [1, 2, 3]})

        data = api_handler.get_data_from_api(url=url)

        assert data == [1, 2, 3]


@pytest.mark.parametrize('status_codes', status_codes_for_tests)
def test_mock_get_data_from_api_should_be_void_response(status_codes):

    with requests_mock.Mocker() as mocker:
        url = 'https://rickandmortyapi.com/api/'

        mocker.get(url,
                   status_code=status_codes,
                   json=[1, 2])

        data = api_handler.get_data_from_api(url=url)

        assert data == []

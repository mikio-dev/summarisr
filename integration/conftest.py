# pylint: disable=W0613
import os

import pytest
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()

pytest_plugins = ["docker_compose"]


@pytest.fixture
def client(module_scoped_container_getter):

    # Get the environment variables
    hostname = os.environ.get("TEST_HOSTNAME")
    port = os.environ.get("TEST_PORT")
    api_v1_str = os.environ.get("API_V1_PATH")

    # Wait for the api to become responsive
    request_session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    request_session.mount("http://", HTTPAdapter(max_retries=retries))

    base_url = f"http://{hostname}:{port}"
    assert request_session.get(base_url)

    api_url = f"{base_url}{api_v1_str}"
    return request_session, api_url

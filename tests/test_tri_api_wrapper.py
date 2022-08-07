beth_athlete_id = 117212

from pytest import fixture
from tri_api_wrapper import Athlete

@fixture
def athlete_info_keys():
    # Responsible only for returning the test data for athlete info endpoint
    return ['code', 'success', 'data']

def test_athelte_info():
    """Tests an API call to get an athletes info"""

    athlete_instance = Athlete(beth_athlete_id)
    response = athlete_instance.info()

    assert isinstance(response, dict)
    assert response['athlete_id'] == beth_athlete_id, "The ID should be in the response"
    assert set(athlete_info_keys).issubset(response.keys()), "All keys should be in the response"
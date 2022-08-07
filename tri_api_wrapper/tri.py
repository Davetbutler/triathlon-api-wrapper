from . import session
from tri_api_wrapper import TRI_API_KEY

class API(object):
  def __init__(self):
      self.token = TRI_API_KEY
      self.headers = {"Accept": "application/json", "apikey": f"{self.token}"}

  def get(self, url, params=None):
      self.url = url
      self.params = params
      response = session.get(url=url, headers=self.headers, params=self.params)
      status_code = response.json()["code"]
      # if the status code is not 200 raise an exception
      if status_code != 200:
          raise Exception(f"API status code returned: {status_code}. For url - {url} and token - {self.token}")
      return response

class Athlete(object):
  def __init__(self, id):
      self.id = id

  def info(self):
      api = API()
      url = f'https://api.triathlon.org/v1/athletes/{self}'
      response = api.get(url)
      return response.json()


class AthleteListings(object):


    def listings(self, catagory_id, gender, elite):
        self.params = {
            "catagory_id": catagory_id,
            "gender": gender,
            "elite": elite
        }
        api = API()
        url = "https://api.triathlon.org/v1/athletes"
        response = api.get(url=url, params=self.params)
        return response

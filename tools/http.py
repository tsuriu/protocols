import requests


class http(object):
    """This class must to be the http request module."""

    def __init__(self, base_url, headers=None):
        """Start method."""
        self.base_url = base_url    
        if headers is not None:
            self.headers = headers

    def get(self, endpoint=None, payload=None):
        """Get method."""
        if endpoint is not None:
            url = self.base_url+endpoint

        try:
            res = requests.get(url, data=payload, headers=self.headers)
            res =  res.json()
        except requests.exceptions.RequestException as error:
            res = error

        return res

    def post(self, endpoint=None, payload=None):
        """Post method."""
        if endpoint is not None:
            url = self.base_url+endpoint

        try:
            res = requests.post(url, data=payload, headers=self.headers)
            res = res.json()
        except requests.exceptions.RequestException as error:
            res = error

        return res
from core import Log
from core.Assert import Assertion
from core.rest_client import RestClient


class BaseApi:
    def __init__(self):
        self.Logger = Log.LogInfo()
        self.Assert = Assertion()
        self.rest_client = RestClient()

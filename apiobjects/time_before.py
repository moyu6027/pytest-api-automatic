from apiobjects.base_api import BaseApi


class Time(BaseApi):

    def before_api(self, payload, env_config):
        url = env_config['host']['url']
        return self.rest_client.requests(host=url, url='/time/before', method='GET', params=payload)

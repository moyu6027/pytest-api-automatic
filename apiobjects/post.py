from apiobjects.base_api import BaseApi


class Post(BaseApi):

    def post_param(self, payload, env_config):
        url = env_config['host']['url']
        return self.rest_client.requests(host=url, url='/post', method='POST', data=payload)

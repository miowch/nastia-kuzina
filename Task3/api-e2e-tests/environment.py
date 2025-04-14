import os
 
 
class Environment:
    LOCAL = 'local'

    URLS = {
        LOCAL: os.getenv("API_BASE_URL", 'http://localhost:8080/api/v3')
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.LOCAL

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


ENV_OBJECT = Environment()
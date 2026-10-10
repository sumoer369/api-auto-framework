import requests
import yaml

class RequestUtil:
    def __init__(self):
        with open("config/config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        env = config["active_env"]
        self.base_url = config["env"][env]["base_url"]
        self.timeout = config["env"][env]["timeout"]

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, timeout=self.timeout)

    def post(self, endpoint, json=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, timeout=self.timeout)
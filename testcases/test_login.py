import pytest
import yaml
from api.login_api import LoginApi


def load_cases():
    with open("data/login_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize("case", load_cases())
def test_get_api(case):
    api = LoginApi()

    if case["endpoint"] == "/posts":
        response = api.get_all_posts()
    else:
        post_id = case["endpoint"].split("/")[-1]
        response = api.get_post(post_id)

    print(f"执行用例: {case['case_name']} -> 状态码: {response.status_code}")
    assert response.status_code == case["expected_status"]
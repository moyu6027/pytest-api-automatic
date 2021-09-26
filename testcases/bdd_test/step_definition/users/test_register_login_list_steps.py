from pytest_bdd import scenarios, given, when, then, parsers
import os
from core.constant import Constant

feature_path = os.path.join(Constant.FEATURE_DIR, "users", "register_login_list.feature")
scenarios(feature_path)


@given('Sean have been authorized')
def register_user():
    print("register_user")


@when('Access user "<path>" API')
def login_user(path):
    print("login_user {}".format(path))


@then('The status code should be "<status_code>"')
def verify_status_code(status_code):
    print("verify_status_code {}".format(status_code))


@then('The response should correct format')
def verify_response():
    print("The response should correct format")

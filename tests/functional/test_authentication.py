import pytest
from pytest_bdd import scenario, given, when, then

from utils.passwords import authenticate

@scenario(scenario_name='valid authentication', feature_name='authentication')
def test_authentication():
	pass

@pytest.fixture
def username():
    return "root"

@pytest.fixture
def password():
    return "password"

@given('I am root user')
def start_user(username):
	return dict(user=username)

@given('Password is root')
def start_password(start_user, password):
	start_user['password'] = 'root'

@when('I try to authenticate')
def auth(start_user):
	start_user['hash']='hashed'

@then('password hash must match')
@then('I should get return as True')
def should_authentication_match(start_user):
	assert authenticate(start_user['user'], start_user['password']) == True

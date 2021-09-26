import pytest


@pytest.fixture(scope="function")
@pytest.mark.datafile("scenario_test_data.yml")
def testcase_data(request, parameters):
    testcase_name = request.function.__name__
    return parameters
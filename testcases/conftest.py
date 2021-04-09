import pytest
import logging


@pytest.fixture(scope='package', autouse=True)
def testsuite_setup_teardown():
    logging.info('------------------------------------- Start to run test case ---------------------------------\n')
    yield
    logging.info('------------------------------------- End to run test case------------------------------------')
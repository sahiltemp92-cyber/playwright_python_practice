# Fixtures
import pytest


@pytest.fixture(scope="function")
def prework():
    print("preWork: I setup browser instance")

def test_initial_check(prework):
    print("This is the first test")


def test_second_check(prework):
    print("This is the second test")

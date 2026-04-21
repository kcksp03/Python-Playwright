import pytest

# Fixtures
# - provide a way to create reusable setup code, which can be used across multiple test cases
# function - runs before every test function
# module - runs only once before all the tests in the same file
# class - runs only once before all the tests in the class file
# session - runs only once across the whole execution

@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup function instance")
    yield # pause -- browser closing/cookie deletion
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print ("This is first test")
    assert preWork == "fail"

@pytest.mark.skip
def test_secondCheck(preSetupWork, secondWork):
    print ("This is second test")

import  pytest

@pytest.fixture(scope="function")           #when scope="session" it will run for that entire session in whole setup  
def preSetupWork():
    print(" \n I setup browser instance")

import  pytest


@pytest.fixture(scope="module")             #when scope = "module" fixture only runs once at start 
                                            #but when its "function" it will each time when they have been called
def preWork():
    print(" \n I setup module browser instance")

@pytest.fixture(scope="function")             #when scope = "module" fixture only runs once at start 
                                            #but when its "function" it will each time when they have been called
def secondWork():
    print(" \n I setup secondWork browser instance")
    yield                              # first do above then pause here then run cases then run whatever after yield
    print("teardown validation")


def test_intialCheck(preWork , secondWork):
    print("This is First Test")

def test_secondCheck(preWork , secondWork):
    print("This is Second Test")
import  pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium", help="Browser name to run tests"
    )

@pytest.fixture(scope='session')
def user_credentails(request):
    return request.param

@pytest.fixture(scope='session')
def browser_Instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
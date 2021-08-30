def pytest_addoption(parser):
    parser.addoption("--url", action="store")


def pytest_generate_tests(metafunc):
    # This is called for every test.
    option_value = metafunc.config.option.url
    if 'url' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("url", [option_value])
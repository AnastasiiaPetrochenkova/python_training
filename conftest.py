from fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application(request)
        fixture.session.login(user_name='admin', password='secret')
    else:
        if not fixture.is_valid():
            fixture = Application(request)
            fixture.session.login(user_name='admin', password='secret')
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

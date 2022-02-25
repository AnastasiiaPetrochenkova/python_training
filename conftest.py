from fixture.application import Application
import pytest

@pytest.fixture(scope= 'session')
def app(request):
    fixture = Application(request)
    request.addfinalizer(fixture.destroy)
    return fixture
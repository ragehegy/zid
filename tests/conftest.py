import pytest

@pytest.fixture(scope='module')
@pytest.mark.django_db
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        yield

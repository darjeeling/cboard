import pytest

@pytest.mark.django_db
def test_test():
    from board.models import Posts
    assert 1 == 1

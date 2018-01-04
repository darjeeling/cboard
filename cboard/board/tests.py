import pytest
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

@pytest.mark.django_db
def test_test():
    from board.models import Post
    user = mommy.make('User', username='test1', is_active=True)
    user.set_password('test')
    user.save()
    post = mommy.make('Post')
    assert 1 == 1

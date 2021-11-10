import pytest

from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(
        title="pytest with factory", status=1, content="that's MY test"
    )


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == "pytest with factory"
    assert post_published.status == 1
    assert post_published.author.username is not None
    assert post_published.author.email is not None
    assert post_published.content == "that's MY test"


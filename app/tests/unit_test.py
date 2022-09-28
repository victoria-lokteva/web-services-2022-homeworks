import pydantic
import pytest
from ..registration import User
from ..tasks import Task


@pytest.mark.parametrize("login, exception_check",
                         [('mike', pytest.raises(pydantic.ValidationError)),
                          ('savva!39', pytest.raises(pydantic.ValidationError)),
                          (123490, pytest.raises(pydantic.ValidationError)),
                          ('mike1997', pytest.not_raises()),
                          ('mikhailodintsov', pytest.not_raises()),
                          ])
def test_user_login(login: str, exception_check):
    with exception_check:
        User(login=login)


@pytest.mark.parametrize("password, exception_check",
                         [('ssssssss', pytest.raises(pydantic.ValidationError)),
                          ('12345', pytest.raises(pydantic.ValidationError)),
                          ('stepan_razin1', pytest.raises(pydantic.ValidationError)),
                          ('Wordlcup2018', pytest.not_raises()),
                          ('BremeN_123', pytest.not_raises()),
                          ])
def test_user_password(password: str, exception_check):
    with exception_check:
        User(password=password)


@pytest.mark.parametrize("task, exception check",
                         [('omg', pytest.raises(pydantic.ValidationError)),
                          (12345, pytest.raises(pydantic.ValidationError)),
                          ('To do homework', pytest.not_raises())])
def test_task(task_description: str, exception_check):
    with exception_check:
        Task(task_description=task_description)

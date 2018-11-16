import pytest
import timedelta
from django.test import TestCase

from TaskList.forms import TaskEditForm
from TaskList.tests.factories import UserFactory
from TaskList

pytestmark = pytest.mark.django_db


class TestTaskCreationForm:

    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = TaskEditForm(
            {
                "name": "oops",
                "description": "hi",
                "start": start,
                "end": end,
                "done": done,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a task.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = TaskEditForm(
            {
                "name": name,
                "description": description,
                "start": start,
                "end": end,
                "done": done,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors

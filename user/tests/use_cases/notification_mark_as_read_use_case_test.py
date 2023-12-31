from unittest.mock import Mock

from app.application.use_cases import NotificationMarkAsReadUseCase


class TestNotificationMarkAsCreateUseCase:
    def test_it_must_be_possible_to_mark_a_notification_as_read(self):
        repository = Mock()
        repository.mark_as_read.return_value = {"state": False}
        sut = NotificationMarkAsReadUseCase(repository)

        notification_data = sut.execute(id=1)

        assert notification_data["state"] == False

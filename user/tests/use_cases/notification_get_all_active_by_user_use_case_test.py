from unittest.mock import Mock

from app.application.use_cases import NotificationGetAllActiveByUserUseCase


class TestNotificationGetAllActiveByUserUseCase:
    def test_it_must_be_possible_to_get_notifications_list(self):
        repository = Mock()
        repository.get_all_by_user_id.return_value = [
            {"id": 1, "title": "Notification 1", "description": "Description 1"},
            {"id": 2, "title": "Notification 2", "description": "Description 2"},
        ]

        sut = NotificationGetAllActiveByUserUseCase(repository)

        notification_data = sut.execute(user_id=1)

        assert len(notification_data) == 2
        assert notification_data[0]["title"] == "Notification 1"
        assert notification_data[1]["title"] == "Notification 2"

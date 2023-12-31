from unittest.mock import Mock

from app.application.use_cases import NotificationCreateUseCase


class TestNotificationCreateUseCase:
    def test_it_must_be_possible_to_create_a_notification(self):
        title = "Notification user"
        description = "asdasdasd asdasd asdasd"

        repository = Mock()
        repository.create.return_value = {
            "id": 1,
            "title": title,
            "description": description,
            "state": True,
            "user_id": 1,
        }
        sut = NotificationCreateUseCase(repository)

        notification_data = sut.execute(
            {
                "title": title,
                "description": description,
                "user_id": 1,
            }
        )

        assert notification_data["id"] == 1
        assert notification_data["title"] == title
        assert notification_data["description"] == description
        assert notification_data["user_id"] == 1

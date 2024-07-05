#Николай Подобед, 18-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def positive_assert():
    track_number = sender_stand_request.create_order()
    response_track = sender_stand_request.get_order_by_track(track_number)
    assert response_track.status_code == 200


def test_order():
    positive_assert()

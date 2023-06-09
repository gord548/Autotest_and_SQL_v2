# Евгения Гордеева, 5-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_order_info_success_response():
    response = sender_stand_request.get_order()
    assert response.status_code ==200
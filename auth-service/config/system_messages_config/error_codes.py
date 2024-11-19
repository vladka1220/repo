"""
Модуль для хранения кодов ошибок, используемых в проекте.

Содержит коды ошибок для различных состояний сервера.

Содержимое:
- HTTP_200_OK: Успешный запрос.
- HTTP_201_CREATED: Пользователь успешно зарегистрирован.
- HTTP_400_BAD_REQUEST: Неверные данные запроса.
- HTTP_409_CONFLICT: Конфликт данных, например, при дублирующемся email.
- HTTP_500_INTERNAL_SERVER_ERROR: Ошибка на сервере.
"""

ERROR_CODES = {
    "HTTP_200_OK": 200,
    "HTTP_201_CREATED": 201,
    "HTTP_400_BAD_REQUEST": 400,
    "HTTP_409_CONFLICT": 409,
    "HTTP_500_INTERNAL_SERVER_ERROR": 500,
}

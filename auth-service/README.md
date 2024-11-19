# Auth-Service

## 📚 Оглавление
- [Введение](#введение)
- [Визуальные материалы](#визуальные_материалы)
- [Установка](#установка)
    - [Предварительные требования](#предварительные_требования)
    - [Шаги по установке](#шаги_по_установке)
- [Использование](#использование)
- [Конфигурация](#конфигурация)
- [Тестирование](#тестирование)
- [Поддержка](#поддержка)
- [Планы развития](#планы_развития)
- [Вклад](#вклад)
- [Авторы](#авторы)
- [Лицензия](#лицензия)
- [Статус проекта](#статус_проекта)

## 🚀 Введение
Auth-Service отвечает за авторизацию и регистрацию пользователей в нашей социальной сети. Он реализует следующие функции:

- Регистрация пользователя с электронной почтой и паролем.
- Подтверждение регистрации по электронной почте.
- Интеграция с внешними провайдерами аутентификации (например, Keycloak).
- Управление пользователями через RESTful API.

## 🎬 Визуальные материалы
TBA

## 💾 Установка
### ✔️ Предварительные требования:
1. Python 3.12.5;
2. Требования по библиотекам описаны в файле requirements.txt.

### ✔️ Шаги по установке:
1. Клонируйте репозиторий:

```
git clone https://gitlab.meerkat-code.com/backend/auth-service.git
cd auth-service
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

## 🛠️ Использование
Для работы с Auth-Service вы можете взаимодействовать с API-эндпоинтами для регистрации пользователей, входа в систему и управления данными.

Примеры запросов
Регистрация нового пользователя:

```
curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \'
-d '{"username": "newuser", "email": "newuser@example.com", "password": "password123", "password_confirmation": "password123"}'
```

Вход в систему:

```
curl -X POST http://localhost:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{"username": "existinguser", "password": "password123"}'
```

## ⚙️ Конфигурация
Для корректной работы сервиса необходимо настроить все параметры в файле .env.

## ☣️ Тестирование
Для запуска тестов используйте следующую команду:

```
python manage.py test
```

## 🚑 Поддержка
Если у вас возникли проблемы или вопросы, пожалуйста, обратитесь к команде поддержки через внутреннюю систему отслеживания проблем или отправьте email на адрес поддержки.

## 🔜 Планы развития
- Интеграция многофакторной аутентификации.
- Поддержка дополнительных внешних провайдеров аутентификации.
- Расширенная аналитика и отчетность о пользователях.

## 🤝 Вклад
Если у вас есть предложения по улучшению сервиса, пожалуйста, создайте запрос на изменение через внутреннюю систему управления проектами.  
Для новых функций или исправлений убедитесь, что ваш код соответствует стандартам и проходит тестирование.

## 👋 Авторы
Версия: 1.0  
Ответственный за версию: Дахно Илья

## ©️ Лицензия
Этот проект разработан для внутреннего использования и не предназначен для распространения. Все права защищены.

## ⌛ Статус проекта
Разработка продолжается.... скоро мир увидит новую социальную сеть!

## 📢 Патчноуты самой свежей версии сервиса
v1.0 - подготовлена выгрузка в Main ветку
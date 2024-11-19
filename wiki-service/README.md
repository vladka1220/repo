# Wiki Service

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
- [Патчноуты самой свежей версии сервиса](#патчноуты_самой_свежей_версии_сервиса)

## 🚀 Введение
Wiki-Service предоставляет функционал для создания и управления вики-страницами в социальной сети. 

Основные функции:

- Создание, редактирование и удаление страниц вики.
- Просмотр и поиск статей.
- Управление доступом к статьям через RESTful API.

## 🎬 Визуальные материалы
TBA

## 💾 Установка
### ✔️ Предварительные требования:
1. Python 3.12.5;
2. Требования по библиотекам описаны в файле requirements.txt.

### ✔️ Шаги по установке:
1. Клонируйте репозиторий:

```
git clone https://gitlab.meerkat-code.com/backend/wiki-service.git
cd wiki-service
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv env
source env/bin/activate  # На Windows используйте `env\Scripts\activate`
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

## 🛠️ Использование
Для работы с Wiki-Service вы можете взаимодействовать с API-эндпоинтами для управления вики-страницами.

Примеры запросов:

Создание новой вики-страницы:

```
curl -X POST http://localhost:8000/meerkat_api/wiki_service/ \
-H "Content-Type: application/json" \
-H "Authorization: Token <your_token>" \
-d '{"title": "Sample Page", "content": "This is a sample wiki page content."}'
```

Получение всех страниц вики:

```
curl -X GET http://localhost:8000/meerkat_api/wiki_service/ \
-H "Authorization: Token <your_token>"
```

Получение конкретной вики-страницы:

```
curl -X GET http://localhost:8000/meerkat_api/wiki_service/pages/<page_id>/ \
-H "Authorization: Token <your_token>"
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
- Улучшение интерфейса и пользовательского опыта.

## 🤝 Вклад
Если у вас есть предложения по улучшению сервиса, пожалуйста, создайте запрос на изменение через внутреннюю систему управления проектами.  
Для новых функций или исправлений убедитесь, что ваш код соответствует стандартам и проходит тестирование.

## 👋 Авторы
Версия: 1.0.
Ответственный за версию: Дахно Илья.

## ©️ Лицензия
Этот проект разработан для внутреннего использования и не предназначен для распространения. Все права защищены.

## ⌛ Статус проекта
Разработка продолжается. Ожидаются новые функции и улучшения!

## 📢 Патчноуты самой свежей версии сервиса
v0.1 - подготовлена выгрузка в Main ветку.
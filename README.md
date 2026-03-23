# Yatube API (Kittygram2)

### Описание
Проект представляет собой API для социальной сети Yatube. Он позволяет управлять публикациями, комментариями и подписками через REST-запросы. В проекте реализована аутентификация по токенам и автоматическое определение автора при создании поста.

### Технологии
* **Python 3.9** (важно: версии 3.12+ не поддерживают Django 3.2 из-за удаления `distutils`)
* **Django 3.2.3**
* **Django Rest Framework 3.12.4**
* **SQLite3**

---

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone [https://github.com/yandex-praktikum/kittygram2.git](https://github.com/yandex-praktikum/kittygram2.git)
```
```
cd kittygram2
```
Cоздать и активировать виртуальное окружение (рекомендуется использовать Python 3.9):
```
python3.9 -m venv env
```
```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

Основные эндпоинты API:
POST /api/v1/api-token-auth/ — получение токена аутентификации.

GET /api/v1/posts/ — получение списка всех публикаций.

POST /api/v1/posts/ — создание новой публикации (только для авторизованных пользователей). Автор подставляется автоматически из токена.

GET /api/v1/posts/{id}/ — получение отдельной публикации по её ID.

PUT/PATCH/DELETE /api/v1/posts/{id}/ — редактирование и удаление публикации (доступно только автору).
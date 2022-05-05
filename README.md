# Сервис YaCut

Учебный сервис "YaCut" укоротитель ссылок

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Запуск
- Клонировать репозиторий `git clone`
- Cоздать и активировать виртуальное окружение `python3 -m venv venv` -> `source venv/bin/activate`
- Установить зависимости из файла requirements.txt `pip install -r requirements.txt`
- Запустить сервер `flask run`

## Технологии
- Бэкенд на "Flask + SQLAlchemy"
- Тестирование на "Pytest"
- БД SQLite

## Техническая информация
Вся структура API представлена в [OpenAPI](https://github.com/1kovalevskiy/yacut/blob/3e46472b7023e4de21245a1802a3d1cc01eb8d79/openapi.yml)

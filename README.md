# Тестовое задание

## Настройка перед запуском

Первое, что нужно сделать, это cклонировать репозиторий:
```sh
$ git clone https://github.com/jumabekova06/reviro-io
$ cd reviro-io

```

Создайте виртуальную среду для установки зависимостей и активируйте ее:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Затем установите зависимости:

```sh
(venv)$ pip install -r requirements.txt
```
Запускаем сервер:
```sh

(venv)$ python manage.py runserver
```
навигация для API `http://127.0.0.1:8000/api/v1`.

навигация Get-запроса `http://127.0.0.1:8000/api/Quote`.

но прежде чем просматривать API,создайте суперпользователя
(доступ к Админке):

```sh

(venv)$ python manage.py createsuperuser

путь к админке `http://127.0.0.1:8000/admin/`.

```


были трудности с асинхронным парсингом.